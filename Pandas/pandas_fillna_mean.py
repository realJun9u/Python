import pandas as pd

df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(x, "\n", df.to_string())
