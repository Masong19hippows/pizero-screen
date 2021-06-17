#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from td.client import TDClient

# Create a new session, credentials path is required.
load_dotenv("creds/.env")
key = os.getenv('consumerKey')

TDSession = TDClient(
    client_id=key,
    redirect_uri='https://localhost',
    credentials_path='creds/td_state.json'
)
# Login to the session
TDSession.login()

def price():
    return str(TDSession.get_accounts()[0].get("securitiesAccount").get("currentBalances").get("liquidationValue"))

def percent():
    s = 0
    h = 0
    for item in TDSession.get_accounts(fields=['positions'])[0].get("securitiesAccount").get("positions"):
        amount = item.get("longQuantity") * item.get("averagePrice")
        change = item.get("currentDayProfitLossPercentage")
        h  += amount
        s += change * amount
    average = s / h
    return str(round(average, 2))