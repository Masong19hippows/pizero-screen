import os
from dotenv import load_dotenv
from binance.client import Client

# Loading api key and secret for Binance.US authentication.
load_dotenv("creds/.env")
key = os.getenv('apiKey')
secret = os.getenv('apiSecret')

# This function takes a ticker and calculates how much the account has in USD.
def price(ticker):
    client = Client(key, secret,  tld='us')
    if float(client.get_asset_balance(asset=ticker).get("free")) == 0:
        amount = float(client.get_asset_balance(asset=ticker).get("locked"))
    else:
        amount = float(client.get_asset_balance(asset=ticker).get("free"))
    price = amount * float(client.get_symbol_ticker(symbol=ticker + "USD").get("price"))
    return str(round(price, 2))