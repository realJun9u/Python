import pandas as pd

df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(x, "\n", df.to_string())
