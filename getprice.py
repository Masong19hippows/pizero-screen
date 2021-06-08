import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()
key = os.getenv('apiKey')
secret = os.getenv('apiSecret')

def price(ticker):
    client = Client(key, secret,  tld='us')
    if float(client.get_asset_balance(asset=ticker).get("free")) == 0:
        amount = float(client.get_asset_balance(asset=ticker).get("locked"))
    else:
        amount = float(client.get_asset_balance(asset=ticker).get("free"))
    price = amount * float(client.get_symbol_ticker(symbol=ticker + "USD").get("price"))
    return str(round(price, 2))