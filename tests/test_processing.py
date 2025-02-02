import pytest

from src.processing import filter_by_state, sort_by_date

# Модуль processing

# Тест Функции filter_by_state
@pytest.mark.parametrize('value, expected', [('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),])
def test_filter_by_state_try_state(dict_state, value, expected):
    assert filter_by_state(dict_state, value) == expected


@pytest.mark.parametrize('value, expented', [("EXECUTED", [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),])
def test_filter_by_state_try(dict_state, value, expented):
    assert filter_by_state(dict_state, value) == expented


def test_filter_by_state_try_state_none(dict_state):
    assert filter_by_state(dict_state) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_filter_by_state_none():
    assert filter_by_state("") == "Введенное значение не является списком!"


def test_filter_by_state_invalid_data(long_nums):
    assert filter_by_state(long_nums) == "Введенное значение не является списком!"


# Тест функции sort_by_date
def test_sort_by_date_try(dict_state):
    assert sort_by_date(dict_state) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize('ascending, expented', [(False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                                          {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),])
def test_sort_by_date_try_revers(dict_state, ascending, expented):
    assert sort_by_date(dict_state, False) == expented
