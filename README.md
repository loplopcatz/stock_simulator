# stock_simulator
A stock market simulator with ML, Monte Carlo, and GenAI insights

# 📊 Stock Simulator with ML, Monte Carlo, and GenAI Insight

This project simulates and analyzes stock price movements using real-world data, machine learning, probabilistic simulation (Monte Carlo), and a natural-language summary generator powered by GenAI (OpenAI's GPT-3.5).

---

## 📁 Project Contents

All files are located directly in the root directory:

- `TSLA_stock_data.csv` – input stock data
- `get_stock_data.py` – fetch historical TSLA stock prices from Alpha Vantage
- `predict_stock_trend.py` – logistic regression to predict price up/down
- `monte_carlo_simulation.py` – simulate future price trends
- `genai_stock_analyst.py` – generate financial summary using GenAI
- `.env` – API keys (excluded from version control)
- `.gitignore` – excludes sensitive/cache files
- `README.md` – this documentation
- `requirements.txt` – Python dependencies

---

## 🎯 Features & Goals

| Phase | Feature | What You Learn |
|-------|---------|----------------|
| 📥 Phase 1 | Load + visualize historical TSLA data | Pandas, Matplotlib |
| 🤖 Phase 2 | Predict price direction | Logistic Regression |
| 🎲 Phase 3 | Simulate future prices | Monte Carlo, NumPy |
| 🧠 Phase 4 | Generate insights in natural language | OpenAI GPT-3.5, prompt engineering |

---

## 🛠 Setup

1. **Clone this repo**

```bash
git clone https://github.com/rezafawazul/stock_simulator.git
cd stock_simulator
```

2. **Create a `.env` file** and add your API key:

```env
OPENAI_API_KEY=your_openai_key_here
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Run the AI summary generator:

```bash
python genai_stock_analyst.py
```

If the OpenAI quota is exceeded, it will gracefully fall back to a realistic simulated response.

---

## 📘 What You’ll Learn

- How to connect to financial data APIs and load real stock data
- Predict price direction using Logistic Regression
- Run probabilistic simulations using Monte Carlo methods
- Convert numbers to natural language using GenAI

---

## 🧠 Notes

- This project was developed entirely through iterative collaboration and exploration.
- No third-party dataset or course was used — built from scratch to learn end-to-end AI workflows.

---

## 📄 License

MIT License © 2025 [Reza Fawazul](https://github.com/rezafawazul)
