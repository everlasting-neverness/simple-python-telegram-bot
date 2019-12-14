import requests
from misc import proxies


def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    r = requests.get(url, proxies=proxies).json()
    price = r['ticker']['last']
    return str(price) or '0' + ' usd'
