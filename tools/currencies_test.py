import pytest

from tools.currencies import get_currencies


def test_get_currencies():
    currencies = get_currencies()
    assert 'USD' in currencies.keys()
    assert currencies['USD'] == 'US dollar'