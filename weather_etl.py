from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago
import json

LATITUDE = '51.5074'
LONGITUDE = '-0.1278'
POSTGRES_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

with DAG(
        dag_id='weather_etl_pipeline',
        default_args=default_args, 
        schedule_interval='@daily',
        catchup=False,
        tags=['weather', 'etl'],
        description='Weather data ETL pipeline'
    ) as dag:
    
    @task()
    def extract_weather_data():
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')
        endpoint = f'/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'
        response = http_hook.run(endpoint)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch weather data: {response.status_code}")
        
    @task()
    def transform_weather_data(weather_data):
        current_weather = weather_data['current_weather']
        transformed_data = {
            'latitude': float(LATITUDE),
            'longitude': float(LONGITUDE),
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'winddirection': current_weather['winddirection'],
            'weathercode': current_weather['weathercode']
        }
        return transformed_data
    
    @task()
    def load_weather_data(transformed_data):
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        
        # Create table
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            latitude FLOAT,
            longitude FLOAT,
            temperature FLOAT,
            windspeed FLOAT,
            winddirection FLOAT,
            weathercode INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        # Insert data
        insert_sql = """
        INSERT INTO weather_data (latitude, longitude, temperature, windspeed, winddirection, weathercode)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        pg_hook.run(create_table_sql)
        pg_hook.run(insert_sql, parameters=(
            transformed_data['latitude'],
            transformed_data['longitude'],
            transformed_data['temperature'],
            transformed_data['windspeed'],
            transformed_data['winddirection'],
            transformed_data['weathercode']
        ))

    # Task dependencies
    weather_data = extract_weather_data()
    transformed_data = transform_weather_data(weather_data)
    load_weather_data(transformed_data)