from src.masks import get_mask_card_numder, get_mask_account


# Модуль masks

# Тесты функции get_mask_card_number
def test_get_mask_card_number_try():
    assert get_mask_card_numder('1234567891234567') == '1234 56** **** 4567'


def test_get_mask_card_number_letter():
    assert get_mask_card_numder('12f4567891234567') == "Номер карты не может содержать буквы!"


def test_get_mask_card_number_len_short(short_nums):
    assert get_mask_card_numder(short_nums) == "Вы ввели некорректный номер карты!"


def test_get_mask_card_number_len_long(long_nums):
    assert get_mask_card_numder(long_nums) == "Вы ввели некорректный номер карты!"


def test_get_mask_card_number_type():
    assert get_mask_card_numder(1234567891234567) == 'Введите номер в строчном формате'


# Тесты функции get_mask_account
def test_get_mask_account_try():
    assert get_mask_account("12345678912345678912") == "**8912"


def test_get_mask_account_letter():
    assert get_mask_account("12345g78912345678912") == "Номер счета не может содержать буквы!"


def test_get_mask_account_len_short(short_nums):
    assert get_mask_account(short_nums) == "Вы ввели некорректный номер счета!"


def test_get_mask_account_len_long(long_nums):
    assert get_mask_account(long_nums) == "Вы ввели некорректный номер счета!"


def test_get_mask_account_type():
    assert get_mask_account(12345678912345678912) == 'Введите номер в строчном формате'
