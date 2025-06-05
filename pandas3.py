from pandas2 import housing_data_csv as data

# print(data.loc[data["population"] > 700])
# print(data.loc[data["population"] > 700, ["total_rooms", "total_bedrooms"]])
# print(data.loc[(data["population"] > 700) & (data["median_income"] > 2)])
# print(data.loc[(data["population"] > 700) | (data["median_income"] > 2)])
# print(data[data["households"].isin([606, 277, 237])]["median_income"])

# print(data.query("population > 700"))
# print(data.query("population > 700 and median_income > 2"))
# print(data.query("population > 700 or median_income > 2"))
# print(data.query("households in [606, 345, 717]"))

data_new = data.copy()

# Drop rows 1 and 2 and return a new DataFrame
print(data_new.drop([1, 2]))  # This will return a new DataFrame without rows 1 and 2
data_new.drop(columns=['population'], inplace=True)  # Drop the "income" column in place (modifies data_new directly)

data_new['population'] = data_new['total_rooms'] * 32
print(data_new["population"].head())

print(data_new.rename(columns={"population": "crowd"}, inplace=False).head())