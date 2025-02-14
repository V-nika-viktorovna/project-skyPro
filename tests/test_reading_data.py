from unittest.mock import patch

import pandas as pd

from src.reading_data import get_data_from_csv, get_data_from_excel


@patch('csv.DictReader')
def test_get_data_from_csv_try(get_mock):
    get_mock.return_value = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol',
                              'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                              'description': 'Перевод организации'},
                             {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
                              'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                              'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}
                             ]
    assert get_data_from_csv('C:/Users/PROGRAMM/Downloads/transactions.csv') == [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol',
                                                                                  'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                                                                  'description': 'Перевод организации'},
                                                                                 {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
                                                                                  'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                                                                                  'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}
                                                                                 ]
    get_mock.assert_called_once()


def test_get_data_from_csv_invalid_address():
    assert get_data_from_csv('C:/Users/PROGRAMM/Downloads') == "Ошибка: [Errno 13] Permission denied: 'C:/Users/PROGRAMM/Downloads'"


@patch('pandas.read_excel')
def test_get_data_from_excel_try(get_mock):
    get_mock.return_value = pd.DataFrame([{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol',
                                           'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                           'description': 'Перевод организации'},
                                          {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
                                           'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                                           'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}
                                          ])
    assert get_data_from_excel('C:/Users/PROGRAMM/Downloads/transactions_excel.xlsx') == [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol',
                                                                                           'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                                                                           'description': 'Перевод организации'},
                                                                                          {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
                                                                                           'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                                                                                           'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}
                                                                                          ]
    get_mock.assert_called_once()


def test_get_data_from_excel_invalid_address():
    assert get_data_from_excel('C:/Users/PROGRAMM/Downloads') == "Ошибка: [Errno 13] Permission denied: 'C:/Users/PROGRAMM/Downloads'"
