import argparse
import logging
import os
import time
from dotenv import load_dotenv
from binance.um_futures import UMFutures

# env se key uthao
load_dotenv()
key = os.getenv("API_KEY")
secret = os.getenv("API_SECRET")

# log file ka setup
logging.basicConfig(filename='bot.log', level=logging.INFO)

def run_twap(c, s, side, q, n, wait):
    try:
        one_shot = round(q / n, 4)

        for i in range(n):
            res = c.new_order(
                symbol=s.upper(),
                side=side.upper(),
                type='MARKET',
                quantity=one_shot
            )
            print(f"[{i+1}/{n}] Done ->", res['orderId'])
            logging.info(f"order {i+1}/{n}: {res}")
            time.sleep(wait)
    except Exception as err:
        print("twap fail:", err)
        logging.error("twap error: " + str(err))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--symbol', required=True)
    p.add_argument('--side', required=True, choices=['BUY', 'SELL'])
    p.add_argument('--quantity', type=float, required=True)
    p.add_argument('--intervals', type=int, required=True)
    p.add_argument('--delay', type=int, required=True)

    a = p.parse_args()

    c = UMFutures(key=key, secret=secret, base_url="https://testnet.binancefuture.com")

    run_twap(
        c,
        s=a.symbol,
        side=a.side,
        q=a.quantity,
        n=a.intervals,
        wait=a.delay
    )

# BOT usages like this:
# python src/advanced/twap.py --symbol BTCUSDT --side BUY --quantity 0.01 --intervals 5 --delay 10
# python src/advanced/twap.py --symbol BTCUSDT --side SELL --quantity 0.01 --intervals 5 --delay 10
