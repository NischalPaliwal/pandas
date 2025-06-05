import pandas as pd

housing_data_csv = pd.read_csv('files/california_housing_test.csv')
# print(housing_data_csv.head())

housing_data_csv.to_json('files/california_housing_test.json', index=False)
housing_data_json = pd.read_json('files/california_housing_test.json')
# print(housing_data_json.head())

# print(housing_data_json.sample(10))
# print(housing_data_json.sample(10, random_state=1))

# print(housing_data_csv.loc[78])
# print(housing_data_csv.loc[[23, 24, 25, 26], ['latitude', 'longitude', 'households']])
# print(housing_data_csv.loc[34:67, ['latitude', 'longitude', 'households']])
# print(housing_data_csv.iloc[3:12, 4:6])
# print(housing_data_json[['total_bedrooms', 'population']])
# print(housing_data_csv[6:9])

housing_data_json.loc[5, "housing_median_age"] = 100
# print(housing_data_json.loc[5])

# print(housing_data_csv["housing_median_age"])
# print(housing_data_csv["households"])

# print(housing_data_json.sort_values("housing_median_age", ascending=False))
# print(housing_data_json.sort_values(["housing_median_age", "median_income"], ascending=[False, True]))

# for index, row in housing_data_csv.iterrows():
#   print(index)
#   print(row)
#   print("\n")

# sample response ->
# 2991
# longitude               -117.1700
# latitude                  34.2800
# housing_median_age        13.0000
# total_rooms             4867.0000
# total_bedrooms           718.0000
# population               780.0000
# households               250.0000
# median_income              7.1997
# median_house_value    253800.0000
# Name: 2991, dtype: float64