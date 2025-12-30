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

crypto_trading_bot/
│
├── bot.py                # Main CLI application (menu-driven trading bot)
├── orders.py             # Market, Limit, Stop-Limit order logic
├── logger.py             # Centralized logging
├── test_connection.py    # Verifies Binance Futures Testnet API connection
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── .gitignore            # Excludes venv, .env, cache, logs
│
└── logs/
    └── bot.log           # Execution logs (optional in GitHub)




