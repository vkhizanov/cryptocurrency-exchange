from api_keys import API_KEY, API_SECRET

from bitmex_websocket import BitMEXWebsocket
import logging
from time import sleep


# Basic use of websocket.
def run():
    logger = setup_logger()

    # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                         api_key=API_KEY, api_secret=API_SECRET)

    logger.info("Instrument data: %s" % ws.get_instrument())

    # Run forever
    while ws.ws.sock.connected:
        # logger.info("Ticker: %s" % ws.get_ticker())
        # if ws.api_key:
        #     logger.info("Funds: %s" % ws.funds())
        # logger.info("Market Depth: %s" % ws.market_depth())
        recent_trades = ws.recent_trades()
        print(f"Recent Trades: {recent_trades}")
        print(len(recent_trades))

        sleep(1)


def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    run()
