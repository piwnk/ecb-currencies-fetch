import pytest

from fetch import fetch_currency, get_latest_rate, multiprocessing_fetch


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


@pytest.fixture()
def currencies():
    return multiprocessing_fetch()

def test_multiprocessing_result_is_a_list(currencies):
    assert isinstance(currencies, list)

