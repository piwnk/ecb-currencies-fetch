import pytest

from .fetch import fetch_currency, get_latest_rate, multi_fetch


def test_fetch_usd_successful():
    result = fetch_currency('usd')
    assert 'entries' in result.keys()


def test_fetch_result_contains_rate():
    latest = get_latest_rate('usd')
    assert isinstance(latest, dict)
    assert 'rate' in latest.keys()
    assert isinstance(latest['rate'], float)
    assert latest['rate'] > 0 and latest['rate'] < 5


@pytest.fixture()
def currencies():
    return multi_fetch()

def test_multifetched_currencies_is_a_list(currencies):
    assert isinstance(currencies, list)


def test_multifetched_currencies_contains_usd_rate(currencies):
    usd_details = [cur for cur in currencies if cur['name'] == 'USD']
    assert usd_details
    assert usd_details[0].get('rate')
    assert isinstance(usd_details[0].get('rate'), float)