import argparse
import os
import time
import logging
from binance.um_futures import UMFutures
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("API_KEY")
sec = os.getenv("API_SECRET")

# log file setup
logging.basicConfig(filename="bot.log", level=logging.INFO)

def check_time(c):
    try:
        server = c.time()["serverTime"]
        now = int(time.time() * 1000)
        diff = now - server
        if abs(diff) > 1000:
            print(f"⚠️ Time mismatch: {diff}ms")
            logging.warning("Time sync off: " + str(diff) + "ms")
    except Exception as e:
        print("Couldn't check time:", e)

def market(c, s, d, q):
    try:
        check_time(c)
        res = c.new_order(
            symbol=s.upper(),
            side=d.upper(),
            type="MARKET",
            quantity=q,
            recvWindow=5000
        )
        print("Order done")
        print(res)
        logging.info("Market order: " + str(res))
    except Exception as err:
        print("Error:", err)
        logging.error("Order failed: " + str(err))

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--side", required=True, choices=["BUY", "SELL"])
    p.add_argument("--symbol", required=True)
    p.add_argument("--quantity", required=True, type=float)

    a = p.parse_args()

    c = UMFutures(key=key, secret=sec, base_url="https://testnet.binancefuture.com")
    market(c, a.symbol, a.side, a.quantity)

# BOT usages like this:
# python src/market_orders.py --side BUY --symbol BTCUSDT --quantity 1
# python src/market_orders.py --side SELL --symbol BTCUSDT --quantity 1
