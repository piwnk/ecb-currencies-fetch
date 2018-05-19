import re

CURRENCIES_RAW = """
  US dollar (USD)
  Japanese yen (JPY)
  Bulgarian lev (BGN)
  Czech koruna (CZK)
  Danish krone (DKK)
  Estonian kroon (EEK)
  Pound sterling (GBP)
  Hungarian forint (HUF)
  Polish zloty (PLN)
  Romanian leu (RON)
  Swedish krona (SEK)
  Swiss franc (CHF)
  Icelandic krona (ISK)
  Norwegian krone (NOK)
  Croatian kuna (HRK)
  Russian rouble (RUB)
  New Turkish lira (TRY)
  Australian dollar (AUD)
  Brasilian real (BRL)
  Canadian dollar (CAD)
  Chinese yuan renminbi (CNY)
  Hong Kong dollar (HKD)
  Indonesian rupiah (IDR)
  Indian rupee (INR)
  South Korean won (KRW)
  Mexican peso (MXN)
  Malaysian ringgit (MYR)
  New Zealand dollar (NZD)
  Philippine peso (PHP)
  Singapore dollar (SGD)
  Thai baht (THB)
  South African rand (ZAR)
"""


def get_currencies():
    currencies_split = re.findall(r'([\w ]*) \((\w*)\)', CURRENCIES_RAW)
    return {code: name.strip() for name, code in currencies_split}