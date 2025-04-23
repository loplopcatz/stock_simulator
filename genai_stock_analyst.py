# === PHASE 4: GENAI STOCK ANALYST - TURNING DATA INTO NATURAL LANGUAGE ===
# 🧭 Why we're doing this:
# This phase converts numerical stock data into human-like analysis using a language model (GenAI).
# It simulates what a financial analyst or AI assistant might say based on trends or simulations.
# Useful for dashboards, reports, or creating explainable insights for end users.

# === ✅ PRE-CONDITION ===
# Make sure you've run this command in a safe, active Python environment:
# >>> pip install openai
# Best practice: install inside a conda or virtual environment, NOT system-wide.
# Check your active environment using: conda info --envs or look at the VS Code Python interpreter.

# === 1. IMPORT LIBRARIES ===
import pandas as pd
from datetime import timedelta
from dotenv import load_dotenv
import os
from openai import OpenAI

# === 2. LOAD .env FOR API KEY ===
# This securely loads the OpenAI API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# === 3. SETUP OPENAI CLIENT ===
# Create an instance of the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# === 4. LOAD STOCK DATA ===
# Load the TSLA stock data that we previously saved
file_path = "TSLA_stock_data.csv"
df = pd.read_csv(file_path, parse_dates=['date'])

# === 5. SELECT RECENT PERIOD FOR ANALYSIS ===
# We'll take the last 5 days of closing prices for AI to analyze
recent_data = df.tail(5).copy()

# ✅ Expected Result:
# A small DataFrame showing dates and closing prices from the most recent 5 days

# === 6. FORMAT INTO NATURAL LANGUAGE PROMPT ===
# This creates a prompt that will be sent to the language model
summary_prompt = f"""
You are a financial assistant AI. Based on the closing prices of TSLA over the last 5 days:

{recent_data[['date', 'close']].to_string(index=False)}

Write a short summary about the trend, including if it's going up, down, or fluctuating, and what it might indicate.
"""

# Print the generated prompt to verify its structure
print("\n🧠 Prompt for GenAI:")
print(summary_prompt)

# === 7. SEND PROMPT TO OPENAI API ===
# ⚠️ NOTE: The following block requires active OpenAI quota.
# If your API key is over quota, the fallback response will be triggered instead.
try:
    # We call the chat model to generate a natural-language summary
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": summary_prompt}
        ]
    )
    # (Handled in try block above)
except Exception as e:
    print("⚠️ GenAI API call failed. Fallback activated.")
    print(f"Error: {e}")
    # This fallback message simulates a possible realistic GenAI output
    summary = (
        "📉 Over the past 5 days, TSLA experienced a downward trend followed by a mild rebound. "
        "This may indicate short-term volatility, possible profit-taking, or upcoming consolidation."
    )
# (Handled in try block above)

# === 9. DISPLAY GENERATED ANALYSIS ===
print("\n📣 GenAI Summary:")
print(summary)

# ✅ Expected Result:
# A clear, human-readable summary of the last 5 days of TSLA closing prices — like a financial analyst would write.

# 🧠 What You Just Achieved (Reinforced):
# ✅ Practiced modern prompt engineering using real data
# ✅ Used the latest OpenAI client syntax (v1.0+)
# ✅ Connected a live GenAI model to a data-driven stock analysis workflow
# ✅ Generated natural language insights from structured data
