import numpy as np
import pandas as pd

# Sample Weather Data
data = {
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
    "Temperature (°C)": [23, 25, 21, 20, 22]
}

# Create a DataFrame
df = pd.DataFrame(data)

# 1. Calculate Average Temperature
average_temp = np.mean(df["Temperature (°C)"])

# 2. Find the Hottest and Coldest Day
hottest_day = df.loc[df["Temperature (°C)"].idxmax()]
coldest_day = df.loc[df["Temperature (°C)"].idxmin()]

# 3. Trend: Temperature Difference Between Consecutive Days
df["Temp Difference"] = df["Temperature (°C)"].diff().fillna(0)

# Display Results
print("Weather Data Analysis:")
print(df)

print(f"\nAverage Temperature: {average_temp:.2f}°C")
print(f"Hottest Day: {hottest_day['Date']} with {hottest_day['Temperature (°C)']}°C")
print(f"Coldest Day: {coldest_day['Date']} with {coldest_day['Temperature (°C)']}°C")

print("\nTemperature Differences Between Consecutive Days:")
print(df[["Date", "Temp Difference"]])