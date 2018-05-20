import schedule
from fetch import multi_fetch
from db import insert_rates, connect
from datetime import datetime

CONN_STRING = 'sqlite:///rest/db.sqlite3'

def job():
    try:
        connection = connect(CONN_STRING)
        insert_rates(connection)
        print('Fresh data fetched at {}'.format(datetime.now()))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    job() # initial run
    schedule.every(5).minutes.do(job)
    # schedule.every().day.at("3:00").do(job)
    while True:
        schedule.run_pending()