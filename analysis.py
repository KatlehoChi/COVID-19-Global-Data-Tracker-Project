import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/covid19_data.csv")

# Display dataset overview
print(df.head())
print(df.info())

# Compute basic statistics
print(df.describe())

# Group data by country and compute case averages
country_cases = df.groupby("Country")["Confirmed"].mean()
print(country_cases)

# Line chart: COVID-19 cases over time
df.plot(x="Date", y="Confirmed", kind="line")
plt.title("COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.show()

# Bar chart: Top 10 affected countries
df.groupby("Country")["Confirmed"].sum().nlargest(10).plot(kind="bar")
plt.title("Top 10 Countries by COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.show()
