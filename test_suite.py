import pytest
import benchtest.core
import run

SAMPLE_DATA = {'key1': 'value1', 'key2': 'value2', 'transactions': [{'Date': '2017-11-18', 'Ledger': 'Groceries', 'Amount': '-1.45', 'Company': 'SAFEWAY'}, {'Date': '2017-11-18', 'Ledger': 'Car Loan', 'Amount': '-1323.50', 'Company': 'Loans.ca'}, {'Date': '2017-12-20', 'Ledger': ' ', 'Amount': '2000', 'Company': 'PAYMENT'}]}


def test_http_200():
    """Make sure query URL returns response if HTTP code = 200"""
    query_url_response = benchtest.core.query_url("http://httpbin.org/status/200")
    assert query_url_response.status_code == 200


def test_http_404():
    """Make sure query URL returns response if HTTP code = 404"""
    query_url_response = benchtest.core.query_url("http://httpbin.org/status/404")
    assert query_url_response.status_code == 404


def test_http_exception():
    """Make sure query URL returns exception if HTTP code is not 200 or 404"""
    with pytest.raises(Exception):
        benchtest.core.query_url("http://httpbin.org/status/503")


def test_balance_processor():
    """Make sure balance processor works as expected with sample data"""
    processed_data = {}
    balance_processor_response = benchtest.core.balance_processor(SAMPLE_DATA, processed_data)
    assert balance_processor_response['2017-12-20'] == 2000
    assert sum(balance_processor_response.values()) == 675.05


def test_total_balance():
    """Simply test that final balance is the number we expect"""
    run_response = run.main()
    assert run_response == 18377.16
