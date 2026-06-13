import pandas as pd
df=pd.read_csv("demo.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())