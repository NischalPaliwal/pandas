import pandas as pd

nocs = pd.read_csv('files/noc_regions.csv')
bios = pd.read_csv('files/athlete_events.csv')

merged = pd.merge(bios, nocs, on='NOC', how='inner')
# print(merged.sample(10))

usa = bios[bios['NOC'] == 'USA'].copy()
ind = bios[bios['NOC'] == 'IND'].copy()

new_df = pd.concat([usa, ind])
# print(new_df.head())

print(bios.isna().sum())  # returns the total NaN values per column in the df
print(bios.isna().sample(10))  # returns for each data value whether it is 'NaN' or not in form of 'True' or 'False'

new_bios = bios.fillna(35, inplace=False).copy()
print(new_bios.isna().sum().sum())