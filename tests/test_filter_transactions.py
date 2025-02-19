import pytest

from src.filter_transactions import (filter_transactions_by_description,
                                     filter_transactions_counter_description)


@pytest.mark.parametrize('value, expected', [([{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                                             {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                                             {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
                                             {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': '29482', 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'}],
                                            [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}])
                                            ])
def test_filter_transactions_by_description_try(value, expected):
    assert filter_transactions_by_description(value, 'организации') == expected


def test_filter_transactions_by_description_none():
    assert filter_transactions_by_description([]) == 'Операции не найдены'


def test_filter_transactions_by_description_error():
    assert filter_transactions_by_description('mur') == "Ошибка: 'str' object has no attribute 'get'"


@pytest.mark.parametrize('value, expected', [([{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                                             {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                                             {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
                                             {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': '29482', 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'}],
                                            {'Перевод организации': 1, 'Перевод с карты на карту': 3})
                                            ])
def test_filter_transactions_counter_description_try(value, expected):
    assert filter_transactions_counter_description(value, ['Перевод организации', 'Перевод с карты на карту', 'Перевод со счета на счет']) == expected


def test_filter_transactions_counter_description_none():
    assert filter_transactions_counter_description([]) == 'Операции не найдены'


def test_filter_transactions_counter_description_error():
    assert filter_transactions_by_description('mur') == "Ошибка: 'str' object has no attribute 'get'"
