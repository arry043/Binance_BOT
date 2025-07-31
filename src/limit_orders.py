import argparse
import sys
import logging
import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures

# get keys
load_dotenv()
key = os.getenv("API_KEY")
sec = os.getenv("API_SECRET")

# logs setup
logging.basicConfig(filename="bot.log", level=logging.INFO)

def limit_order(c, sym, s, qty, p):
    try:
        res = c.new_order(
            symbol=sym.upper(),
            side=s.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=qty,
            price=p
        )
        print("Limit order placed")
        print(res)
        logging.info(f"Limit order: {res}")
    except Exception as err:
        print("Limit order failed")
        print(str(err))
        logging.error("Limit order error: " + str(err))

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--symbol", required=True)
    p.add_argument("--side", required=True, choices=["BUY", "SELL"])
    p.add_argument("--quantity", type=float, required=True)
    p.add_argument("--price", required=True)

    args = p.parse_args()

    c = UMFutures(key=key, secret=sec, base_url="https://testnet.binancefuture.com")

    limit_order(
        c,
        args.symbol,
        args.side,
        args.quantity,
        args.price
    )

# BOT usages like this:
# python src/limit_orders.py --symbol BTCUSDT --side BUY --quantity 0.002 --price 60000
# python src/limit_orders.py --symbol BTCUSDT --side SELL --quantity 0.002 --price 60000
