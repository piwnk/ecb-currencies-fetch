import feedparser

URL_TEMPLATE = "https://www.ecb.europa.eu/rss/fxref-{}.html"


def fetch_currency(currency_code):
    return feedparser.parse(URL_TEMPLATE.format(currency_code.lower()))


def get_latest_rate(currency_parsed):
    latest = currency_parsed['entries'][0]
    return {
        "currency": latest['cb_targetcurrency'],
        "rate": float(latest['cb_exchangerate'].split()[0]), 
        "updated": latest['updated']
    }