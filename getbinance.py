import os
from dotenv import load_dotenv
from binance.client import Client

# Loading api key and secret for Binance.US authentication.
dir = os.path.dirname(os.path.realpath(__file__))
load_dotenv(dir + "/creds/.env")
key = os.getenv('binanceKey')
secret = os.getenv('binanceSecret')
client = Client(key, secret,  tld='us')

# This function takes a ticker and calculates how much the account has in USD.
def price():
    price = 0
    for item in client.get_account().get("balances"):
        if float(item.get("free")) == 0 and float(item.get("locked")) == 0:
            continue
        elif float(item.get("locked")) == 0:
            amount = float(item.get("free"))
        else:
            amount = float(item.get("locked"))
        if item.get("asset") == "USD" or item.get("asset") == "USDT":
            if float(item.get("locked")) == 0:
                amount = float(item.get("free"))
            else:
                amount = float(item.get("locked"))
            price += amount
        else:
            price += amount * float(client.get_symbol_ticker(symbol=item.get("asset") + "USD").get("price"))
    return str(round(price, 2))

def percent():
    sumHave = 0
    s = 0
    for item in client.get_account().get("balances"):
        free = float(item.get("free"))
        locked = float(item.get("locked"))
        asset = item.get("asset")
        if free == 0 and locked == 0:
            continue
        elif asset == "USD" or asset == "USDT":
            if locked == 0:
                amount = free
            else:
                amount = locked
            sumHave += amount
            continue
        else:
            t = client.get_ticker(symbol=asset + "USD")
            if locked == 0:
                amount = free
            else:
                amount = locked
        h = float(t.get("lastPrice")) * amount
        p = float(t.get("priceChangePercent"))
        sumHave += h
        s += p * h
    return str(round(s / sumHave, 2))