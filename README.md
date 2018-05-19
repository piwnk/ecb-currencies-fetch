.tools/:
1.  currencies.py - simple function to get available currencies list
2.  fetch.py:
    *   fetch_currency - func to parse RSS from url, currency code as a parameter
    *   get_latest_rate - func to get latest rate from fetch result (of 5 latest rates)
    *   multi_fetch - func to make paralel request to get all currencies
3.  currencies_test.py, fetch_test.py - unit tests

./:
1.  api.py - simple flask API with localhost:5000/api/currencies route launching multi_fetch function.