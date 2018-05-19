import feedparser
from multiprocessing import Pool

from .currencies import get_currencies

URL_TEMPLATE = "https://www.ecb.europa.eu/rss/fxref-{}.html"


def fetch_currency(currency_code):
    return feedparser.parse(URL_TEMPLATE.format(currency_code.lower()))


def get_latest_rate(currency_code):
    fetch_result = fetch_currency(currency_code)
    latest = fetch_result['entries'][0]
    return {
        "currency": latest['cb_targetcurrency'],
        "rate": float(latest['cb_exchangerate'].split()[0]),
        "updated": latest['updated']
    }


def multi_fetch():
    currencies = [code for code in get_currencies().keys()]
    pool = Pool(processes=4)

    result = pool.map(get_latest_rate, currencies)

    pool.close()
    pool.join()

    return result