from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, DateTime
from sqlalchemy.sql import bindparam
from dateutil import parser as date_parser

from tools.fetch import multi_fetch


def connect(conn_string):
    try:
        return create_engine(conn_string).connect()
    except Exception as e:
        print(e)
        return


def insert_rates(connection):
    if not connection:
        return
        
    metadata = MetaData(connection)
    CurrencyRates = Table('restapp_currencyrates', metadata,
        Column('name', String(3)),
        Column('rate', Float),
        Column('updated', DateTime),
    )

    fetch_results = multi_fetch()

    fetch_results = [{
        **result,
        'updated': date_parser.parse(result['updated'])
        } for result in fetch_results]

    d = CurrencyRates.delete()
    i = CurrencyRates.insert()
    connection.execute(d)
    connection.execute(i, fetch_results)
    connection.close()
