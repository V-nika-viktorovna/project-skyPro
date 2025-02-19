import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('value, expected', [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                             ('Счет 64686473678894779589', 'Счет **9589'),
                                             ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                             ('Счет 35383033474447895560', 'Счет **5560'),
                                             ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                             ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                             ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                                             ('Счет 73654108430135874305', 'Счет **4305'),
                                             ]
                         )
def test_mask_account_card_try(value, expected):
    assert mask_account_card(value) == expected


def test_mask_account_card_none():
    assert mask_account_card("") == "Вы ввели некоректный номер карты или счета"


def test_mask_account_card_len_short(short_nums):
    assert mask_account_card(short_nums) == "Вы ввели некоректный номер карты или счета"


def test_mask_account_card_len_long(long_nums):
    assert mask_account_card(long_nums) == "Вы ввели некоректный номер карты или счета"


def test_mask_account_card_none_account():
    assert mask_account_card("12345678912345678912") == "**8912"


def test_mask_account_card_card():
    assert mask_account_card("Maestro") == "Вы ввели некоректный номер карты или счета"


# Тест функции get_data
def test_get_data_try():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_data_none():
    assert get_date("") == "Вы не ввели дату"


def test_get_data_correct_format_short(short_nums):
    assert get_date(short_nums) == "Вы не ввели дату"


def test_get_data_correct_format_long(long_nums):
    assert get_date(long_nums) == "Неверный формат даты"
