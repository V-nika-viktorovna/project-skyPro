from unittest.mock import patch

from src.external_api import get_transaction_amount_rub


@patch('requests.get')
def test_get_transaction_amount_rub_try_usd(mock_get, transact):
    mock_get.return_value.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 9824.07}, 'info': {'timestamp': 1738744983, 'rate': 98.954297}, 'date': '2025-02-05', 'historical': True, 'result': 972133.940529}
    assert get_transaction_amount_rub(transact) == '972133.94 RUB'
    mock_get.assert_called_once()


@patch('requests.get')
def test_get_transaction_amount_rub_try_eur(mock_get, transact_eur):
    mock_get.return_value.json.return_value = {'success': True, 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 9824.07}, 'info': {'timestamp': 1738746663, 'rate': 102.317602}, 'date': '2025-02-05', 'historical': True, 'result': 1005175.28428}
    assert get_transaction_amount_rub(transact_eur) == '1005175.28 RUB'
    mock_get.assert_called_once()


def test_get_transaction_amount_rub_try():
    assert get_transaction_amount_rub({
                                       "id": 41428829,
                                       "state": "EXECUTED",
                                       "date": "2019-07-03T18:35:29.512364",
                                       "operationAmount": {
                                            "amount": "9824.07",
                                            "currency": {
                                                "name": "RUB",
                                                "code": "RUB"
                                            }
                                       },
                                       "description": "Перевод организации",
                                       "from": "MasterCard 7158300734726758",
                                       "to": "Счет 35383033474447895560"
                                       }) == '9824.07 RUB'


def test_get_transaction_amount_rub_unspecified_currency():
    assert get_transaction_amount_rub({
                                        "id": 41428829,
                                        "state": "EXECUTED",
                                        "date": "2019-07-03T18:35:29.512364",
                                        "operationAmount": {
                                            "amount": "9824.07",
                                            "currency": {
                                                "name": "BY",
                                                "code": "BY"
                                            }
                                        },
                                        "description": "Перевод организации",
                                        "from": "MasterCard 7158300734726758",
                                        "to": "Счет 35383033474447895560"
                                        }) == '9824.07 BY, данная валюта не конвертируется'


def test_get_transaction_amount_rub_none():
    assert get_transaction_amount_rub() == 'Транзакций не найдено'
