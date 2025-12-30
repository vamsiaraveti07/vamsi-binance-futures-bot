# Binance Futures Testnet Trading Bot (Python)

A command-line based **Binance Futures Testnet trading bot** built using Python.
This project demonstrates real-world API integration, futures order execution,
and clean software engineering practices.

---

## ✨ Features

- ✅ Binance **Futures Testnet** integration
- 📈 Place **Market Orders**
- 📉 Place **Limit Orders**
- 🛑 Place **Stop-Limit Orders** (Risk Management – Bonus)
- 💼 View USDT account balance
- 📊 View open futures positions
- 🖥️ Menu-driven **CLI interface**
- 🧾 File-based logging for all orders and errors

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **API:** Binance Futures REST API (Testnet)
- **Library:** python-binance
- **Architecture:** Modular (bot, orders, logger)

---

## 📂 Project Structure

```text
crypto_trading_bot/
│
├── bot.py                # Main CLI application (menu-driven trading bot)
├── orders.py             # Market, Limit, Stop-Limit order logic
├── logger.py             # Centralized logging
├── test_connection.py    # Verifies Binance Futures Testnet API connection
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── .gitignore            # Excludes venv, .env, cache, logs

```
---
# Setup & Installation
## 1.Install dependencies
    pip install -r requirements.txt
## 2.Verify API connection
    python test_connection.py
## Expected output:
CONNECTED TO BINANCE FUTURES TESTNET
USDT Balance: 5000
## 3.Run the trading bot
    python bot.py
# CLI Menu Preview
1. Place Market Order
2. Place Limit Order
3. Place Stop-Limit Order
4. View USDT Balance
5. View Open Positions
6. Exit
# 🧾 Sample Log Output
```text
2025-12-30 | INFO | MARKET | BTCUSDT | BUY | qty=0.002 
2025-12-30 | INFO | STOP-LIMIT | BTCUSDT | BUY | stop=43000 | limit=43100
```
# 🔒 Security Practices

API keys are never committed to source control

.env, venv, cache files are excluded via .gitignore

Withdraw permissions disabled

Testnet environment used (no real funds)
# 📌 Disclaimer
This project is created for educational and internship assessment purposes only.
No financial or trading advice is provided.












