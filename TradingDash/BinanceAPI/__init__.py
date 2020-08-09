import datetime
import logging

import azure.functions as func
from binance.client import Client
from binance import BinanceAPIException

api_key = "SECRET API KEY"
api_secret = "SECRET API KEY"
client = Client(api_key, api_secret, {"verify": False, "timeout": 20})

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    try:
        info = client.get_account()
        #balanceBTC = client.get_asset_balance(asset='ETH')
        status = client.get_account_status()
        print(info)
        print(status)
    except BinanceAPIException as e:
        print(e.status_code)
        print(e.message)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
