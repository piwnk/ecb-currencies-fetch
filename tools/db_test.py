import pytest

from tools.db import connect, insert_rates

CONN_STRING = 'sqlite:///rest/db.sqlite3'


def test_connection_valid():
    assert connect(CONN_STRING)