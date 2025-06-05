import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'], index=['x', 'y', 'z'])
df.head()  # print
df.head(1)  # print
df.head(2)  # print
df.tail(1)  # print

df.index.to_list()  # print
df.columns.tolist()  # print
df.info()  # print(df.info()) will print 'None' as info() func does not return anything

df.describe()  # print
df.nunique(axis=0)  # print (used to count the number of unique values)
df.nunique(axis=1)  # print (used to count the number of unique values)

print(df.shape)
print(df.size)