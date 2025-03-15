import pandas as pd 

data = pd.read_csv("titanic.csv")

# print(data)

missing_values = data.isnull().sum()

mean_age = data["Age"].mean()

mean_age_by_sex = data.groupby("Sex")[["Age"]].mean()

total_passangers = len(data)
total_survivors = data["Survived"].sum()
survivor_percentage = (total_survivors/ total_passangers)*100

print(missing_values)
print(mean_age_by_sex)
print(mean_age)
print(survivor_percentage)