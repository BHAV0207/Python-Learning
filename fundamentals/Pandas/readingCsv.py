import pandas as pd 

df = pd.read_csv("employees.csv")

print(df.head())
# print(df)

print(df["Age"])

df_filtered = df[df["Age"] >= 35]

print(df_filtered)