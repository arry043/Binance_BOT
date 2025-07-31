import argparse
import logging
import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures

load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

logging.basicConfig(filename='bot.log', level=logging.INFO)

def place_oco(client, symbol, side, qty, tp, sl):
    try:
        opp = 'SELL' if side=='BUY' else 'BUY'

        # TP order
        tp_order = client.new_order(
         symbol=symbol,
         side=opp,
         type="LIMIT",
         timeInForce="GTC",
         quantity=qty,
         price=tp
        )
        logging.info(f"TP order done: {tp_order}")
        print("Take profit placed")
        print(tp_order)

        # SL order
        sl_order = client.new_order(
         symbol=symbol,
         side=opp,
         type="STOP_MARKET",
         stopPrice=sl,
         quantity=qty,
         priceProtect=True
        )
        logging.info(f"SL placed: {sl_order}")
        print("Stop loss placed")
        print(sl_order)

    except Exception as e:
        logging.error(f"OCO order failed: {e}")
        print("Some error occurred while placing OCO:")
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', required=True)
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'])
    parser.add_argument('--quantity', required=True, type=float)
    parser.add_argument('--tp', required=True)
    parser.add_argument('--sl', required=True)

    a = parser.parse_args()

    client = UMFutures(
        key=api_key,
        secret=api_secret,
        base_url="https://testnet.binancefuture.com"
    )

    place_oco(
        client,
        symbol=a.symbol.upper(),
        side=a.side.upper(),
        qty=a.quantity,
        tp=a.tp,
        sl=a.sl
    )

# BOT usages like this:
# python src/advanced/oco.py --symbol BTCUSDT --side BUY --quantity 0.002 --tp 62000 --sl 57000 
# python src/advanced/oco.py --symbol BTCUSDT --side SELL --quantity 0.002 --tp 62000 --sl 57000  
