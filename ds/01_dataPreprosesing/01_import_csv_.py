import pandas as pd

df = pd.read_csv("datasets.csv")
print(df)
print(df[['Gender', 'Income','Education Level']])
