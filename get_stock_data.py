# === 1. IMPORT REQUIRED MODULES ===
# 🎯 SKILLS: Python basics, API handling, .env security, web requests, and data parsing
# 💡 GOALS: API Integration, Data Preprocessing
import os
from dotenv import load_dotenv
import requests
import pandas as pd  # For data handling and analysis

# === 2. LOAD ENVIRONMENT VARIABLES ===
# 🎯 SKILL: Load sensitive data securely
# 💡 GOAL: Using .env securely + PyCharm/VS Code practice
load_dotenv()
API_KEY = os.getenv("ALPHA_API_KEY")

# === 3. SET API ENDPOINT FOR STOCK DATA ===
# 🎯 SKILL: Working with web APIs and real data
# 💡 GOAL: Data Collection via API
symbol = "TSLA"  # Tesla
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

# === 4. SEND API REQUEST ===
# 🎯 SKILL: Using `requests` to access external data
# 💡 GOAL: API Integration
response = requests.get(url)

# === 5. HANDLE AND PARSE RESPONSE ===
# 🎯 SKILL: JSON parsing
# 💡 GOAL: Early Data Cleaning
if response.status_code == 200:
    data = response.json()

    if "Time Series (Daily)" in data:
        print(f"✅ Successfully fetched stock data for {symbol}")

        # === 6. EXTRACT AND FORMAT TIME SERIES DATA ===
        # 🎯 SKILLS: Convert JSON to structured data
        # 💡 GOAL: Data Preprocessing, Pandas Basics
        raw_timeseries = data["Time Series (Daily)"]
        df = pd.DataFrame.from_dict(raw_timeseries, orient='index')

        # 🎯 SKILL: Rename columns for readability
        # 💡 GOAL: Data Cleaning
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df.index.name = "date"

        # 🎯 SKILL: Clean and sort index
        # 💡 GOAL: Data Preprocessing, Sorting, Formatting
        df.sort_index(inplace=True)

        # 🎯 SKILL: Convert string values to float
        # 💡 GOAL: Data Transformation
        df = df.astype(float)

        # 🎯 SKILL: Quick EDA
        # 💡 GOAL: EDA (exploratory data analysis)
        print("\n📊 Data Preview:")
        print(df.head())

        # === 7. SAVE CLEANED DATA ===
        # 🎯 SKILL: Export to CSV
        # 💡 GOAL: Dataset Archiving for ML, Dashboard, etc
        output_file = f"{symbol}_stock_data.csv"
        df.to_csv(output_file)
        print(f"\n💾 Data saved to: {output_file}")

    else:
        print("⚠️ Response received, but no time series data found.")
        print("📦 Response content:")
        print(data)
else:
    print("❌ API request failed. Status code:", response.status_code)
