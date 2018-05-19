import pytest

from fetch import fetch_currency, get_latest_rate


def test_fetch_usd_successful():
    result = fetch_currency('usd')
    assert 'entries' in result.keys()


def test_fetch_result_contains_rate():
    result = fetch_currency('usd')
    latest = get_latest_rate(result)
    assert isinstance(latest, dict)
    assert 'rate' in latest.keys()
    assert isinstance(latest['rate'], float)
    assert latest['rate'] > 0 and latest['rate'] < 5