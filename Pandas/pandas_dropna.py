import pandas as pd

df = pd.read_csv('dirtydata.csv')
print(df.to_string()) # original frame
new_df = df.dropna() # new frame empty cell remove
print(new_df.to_string())
df.dropna(inplace=True) # original frame remove
print(df.to_string())
