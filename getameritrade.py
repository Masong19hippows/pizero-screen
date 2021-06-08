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

def amount():
    return TDSession.get_accounts()[0].get("securitiesAccount").get("currentBalances").get("liquidationValue")