import pandas as pd

df = pd.read_csv('dirtydata.csv')
df.fillna(130, inplace = True)
print(df.to_string())
