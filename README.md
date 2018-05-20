# components
## .tools/:
1.  currencies.py - simple function to get available currencies from list
2.  fetch.py:
    *   fetch_currency - func to parse RSS from url, currency code as a parameter
    *   get_latest_rate - func to get latest rate from fetch result (of 5 latest rates)
    *   multi_fetch - func to make parallel requests to get all currencies
3.  db.py - functions to manage connection and insert new rows to sqlite3
4.  currencies_test.py, fetch_test.py, db_test.py - unit tests
5.  task.py - task scheduled to fetch new data and update currencies table every 10 minutes or at 3am as the rss updates at 1am.
6.  fetch_ondemand_api.py - simple flask API with localhost:5000/api/currencies route launching multi_fetch function.


## ./rest:
1. django app with rest endpoint configured at localhost:8000/api/currencies to fetch data from db.sqlite3

# launch instructions

1. install pipenv if not present

```
pip install pipenv
```

2.  initialize virtualenv

```
pipenv install --three
```

3.  django app with rest endpoint at localhost:8000/api/currencies returning rows from db.sqlite3

```
python rest/manage.py makemigrations
python rest/manage.py migrate
python rest/manage.py createsuperuser
python rest/manage.py runserver
```

4.  flask app with rest endpoint at localhost:5000/api/currencies fetching RSS on demand

```
python tools/fetch_ondemand_api.py
```

5. run scheduler

```
python tools/task.py
```