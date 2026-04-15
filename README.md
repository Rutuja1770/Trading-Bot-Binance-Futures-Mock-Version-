# 📊 Trading Bot – Binance Futures (Mock Version)

⭐ Designed with clean architecture, validation, and logging for production readiness.

---

## 🚀 Overview

This project is a simplified Python trading bot that simulates placing orders on Binance Futures (USDT-M).
It supports MARKET and LIMIT orders with a structured, modular design.

> ⚠️ This version uses a **Mock Client** (no real API required), making it easy to test locally.

---

## ✨ Features

* ✅ Place MARKET and LIMIT orders
* ✅ Supports BUY and SELL sides
* ✅ CLI-based input (command-line arguments)
* ✅ Input validation (symbol, quantity, order type)
* ✅ Logging of requests, responses, and errors
* ✅ Exception handling
* ✅ Clean, reusable code structure

---

## 🏗️ Project Structure

```
trading-bot-binance/
│
├── bot/
│   ├── client.py          # Mock Binance client
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── logs/
│   └── app.log            # Log file
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/trading-bot-binance.git
cd trading-bot-binance
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔹 MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### 🔹 LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
```

---

## 📊 Example Output

```
========================================
📊 ORDER SUMMARY
========================================

{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.01}

✅ Order Placed Successfully!
Order ID: 582193
Status: FILLED
Executed Qty: 0.01
Avg Price: market_price
```

---

## 📝 Logging

Logs are stored in:

```
logs/app.log
```

The log file includes:

* Order requests
* Order responses
* Errors and exceptions

---

## ⚠️ Important Note

This project uses a **Mock Binance Client** instead of real API integration.

### Why?

* No API keys required
* Easy to run and test
* Focus on architecture, validation, and logging

👉 In a real-world scenario, this can be replaced with the official Binance API.

---

## 💡 Assumptions

* Symbol format is valid (e.g., BTCUSDT)
* Quantity must be positive
* Price is required only for LIMIT orders

---

## 🚧 Future Improvements

* Add Stop-Limit order support
* Integrate real Binance API
* Improve CLI UX (interactive prompts)
* Build a simple web UI

---

## 👩‍💻 Author

**Rutuja Sangar**

---

## 📬 Submission Notes

This project was built as part of a Python Developer assignment.
It demonstrates:

* Clean architecture
* Input validation
* Error handling
* Logging practices

---
