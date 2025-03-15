
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = sns.load_dataset("titanic")
print(df)



# Plot histogram for Age
plt.hist(df["age"].dropna(), bins=20, color='purple', edgecolor='black')
# Labels and title
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title("Distribution of Ages on Titanic")



# KDE (Kernel Density Estimation) plot of Age
sns.histplot(df["age"].dropna(), bins=20, kde=True, color="blue")



# Show the plot
plt.show()
