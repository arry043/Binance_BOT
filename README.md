"""
# Binance Futures Trading Bot

## 📌 Features
- Market Orders ✅
- Limit Orders ✅
- OCO (Stop-Loss/Take-Profit) Orders ⚡️
- TWAP Strategy ⚡️
- Logs every action to `bot.log`

## 🛠 Setup
1. Clone the repo or unzip
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run any script from `src/` folder:

### 📈 Market Order
```bash
python src/market_orders.py BTCUSDT BUY 0.01
```

### 📉 Limit Order
```bash
python src/limit_orders.py BTCUSDT SELL 0.01 65000
```

### 🛡️ OCO Order (Stop trigger)
```bash
python src/advanced/oco.py BTCUSDT SELL 0.01 64000 63900
```

### 🕒 TWAP Order
```bash
python src/advanced/twap.py BTCUSDT BUY 0.03 3 10
```
(This splits into 3 orders of 0.01 every 10s)

---

## ⚠️ Note
- Use [Binance Futures Testnet](https://testnet.binancefuture.com) API keys.
- Enable Futures trading access on your key.
- All orders and logs go to `bot.log`

---

## 📄 Report
See `report.pdf` for screenshots and results.

---
"""