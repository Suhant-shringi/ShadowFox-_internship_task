# ==========================================================
# Internship Project
# In-Depth AQI Analysis of Delhi
# Shows Data + Graphs
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use("seaborn-v0_8")
sns.set_palette("coolwarm")

# Create folder to save graphs
if not os.path.exists("graphs"):
    os.makedirs("graphs")

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("delhiaqi.csv")

# Rename columns for consistency
df.rename(columns={
    'date': 'Date',
    'co': 'CO',
    'no': 'NO',
    'no2': 'NO2',
    'o3': 'O3',
    'so2': 'SO2',
    'pm2_5': 'PM2.5',
    'pm10': 'PM10',
    'nh3': 'NH3'
}, inplace=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values("Date", inplace=True)

# -----------------------------
# 2. Show sample data
# -----------------------------
print("\n--- Sample Data ---")
print(df.head())

# -----------------------------
# 3. Calculate simplified AQI from PM2.5
# -----------------------------
def calculate_aqi_pm25(pm25):
    if pm25 <= 30:
        return 50 * pm25 / 30
    elif pm25 <= 60:
        return 50 + (50 * (pm25-30)/30)
    elif pm25 <= 90:
        return 100 + (100 * (pm25-60)/30)
    elif pm25 <= 120:
        return 200 + (100 * (pm25-90)/30)
    else:
        return 300 + (200 * (pm25-120)/60)

df['AQI'] = df['PM2.5'].apply(calculate_aqi_pm25)

# -----------------------------
# 4. Data Cleaning
# -----------------------------
df = df.dropna()
df = df.drop_duplicates()

# -----------------------------
# 5. Descriptive Statistics
# -----------------------------
print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\nOverall Mean AQI:", df['AQI'].mean())
print("Maximum AQI:", df['AQI'].max())
print("Minimum AQI:", df['AQI'].min())
print("Standard Deviation:", df['AQI'].std())

# -----------------------------
# 6. AQI Trend Over Time
# -----------------------------
plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['AQI'], color='blue')
plt.title("AQI Trend in Delhi (PM2.5-based)")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/1_AQI_Trend.png")
plt.show()

# -----------------------------
# 7. Monthly Analysis
# -----------------------------
df['Month'] = df['Date'].dt.month
monthly_avg = df.groupby('Month')['AQI'].mean()

print("\n--- Monthly Average AQI ---")
print(monthly_avg)

plt.figure(figsize=(8,5))
monthly_avg.plot(kind='bar', color='orange')
plt.title("Monthly Average AQI in Delhi")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.tight_layout()
plt.savefig("graphs/2_Monthly_AQI.png")
plt.show()

# -----------------------------
# 8. Winter vs Summer Comparison
# -----------------------------
seasons = {"Winter": [11,12,1,2], "Summer": [4,5,6]}

for season_name, months in seasons.items():
    season_data = df[df['Month'].isin(months)]
    if not season_data.empty:
        print(f"{season_name} Average AQI: {season_data['AQI'].mean():.2f}")
    else:
        print(f"{season_name} data not available in dataset")
# -----------------------------
# 9. Pollutant Correlation Analysis
# -----------------------------
pollutants = ['PM2.5', 'PM10', 'NO', 'NO2', 'SO2', 'CO', 'O3', 'NH3']

corr_matrix = df[pollutants + ['AQI']].corr()
print("\n--- Correlation Matrix ---")
print(corr_matrix['AQI'].sort_values(ascending=False))

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Between Pollutants and AQI")
plt.tight_layout()
plt.savefig("graphs/3_Correlation_Heatmap.png")
plt.show()

# -----------------------------
# 10. Rolling Average of AQI
# -----------------------------
df['AQI_Rolling'] = df['AQI'].rolling(window=30).mean()

plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['AQI_Rolling'], color='red')
plt.title("30-Day Rolling Average of AQI")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/4_Rolling_AQI.png")
plt.show()

print("\n✅ Analysis Completed Successfully!")
print("All graphs are saved in the 'graphs/' folder.")
