import pandas as pd

bios = pd.read_csv('files/athlete_events.csv')
# print(bios['City'].value_counts())

coffee = pd.read_csv('files/coffee.csv')
# print(coffee.groupby(['Coffee Type']).agg({'Units Sold': 'sum', 'Day': 'count'}))

pivot = coffee.pivot(index='Day', columns='Coffee Type', values='Units Sold')
# print(pivot.head())

# print(bios.groupby('Year').agg({'Name': 'count'}).reset_index().sort_values('Name'))

coffee['Yesterday Units Sold'] = coffee['Units Sold'].shift(2)
coffee['% Change'] = coffee['Units Sold'] / coffee['Yesterday Units Sold'] * 100
coffee['Units Sold CumSum'] = coffee['Units Sold'].cumsum()
# print(coffee.head())

bios['Age Rank'] = bios['Age'].rank(ascending=True, method='dense')
# print(bios.sort_values('Age Rank', ascending=True).head(7)[['Age', 'Age Rank']])

latte = coffee[coffee['Coffee Type'] == 'Latte'].copy()
latte['Past 3 days revenue'] = latte['Units Sold'].rolling(3).sum() * 60
print(latte.head())