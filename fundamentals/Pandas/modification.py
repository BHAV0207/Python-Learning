import pandas as pd 

data = pd.read_csv("employees.csv")

print(data)

data["bonus"] = data["Salary"]*0.3

print(data)

grouped_data = data.groupby("Age")[["Salary"]].mean()

print(grouped_data)