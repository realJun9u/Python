import pandas as pd

df = pd.read_csv('data2.csv')
print(df.corr()) # 1차 상관계수