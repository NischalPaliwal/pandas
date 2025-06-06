import pandas as pd

bios = pd.read_csv('files/athlete_events.csv')
# print(bios['City'].value_counts())

coffee = pd.read_csv('files/coffee.csv')
# print(coffee.groupby(['Coffee Type']).agg({'Units Sold': 'sum', 'Day': 'count'}))

pivot = coffee.pivot(index='Day', columns='Coffee Type', values='Units Sold')
# print(pivot.head())

# print(bios.groupby('Year').agg({'Name': 'count'}).reset_index().sort_values('Name'))

coffee['Yesterday Units Sold'] = coffee['Units Sold'].shift(2)
print(coffee)