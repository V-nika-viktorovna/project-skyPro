from typing import Iterator


def filter_by_currency(list_transactions: list[dict], currency="") -> Iterator[dict]:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (параметр currency)."""

    list_value = []
    if currency == "":
        yield "Вы не ввели валюту для сортировки транзакций"
    else:
        for transactions in list_transactions:
            for transaction in transactions.keys():
                midl_result = transactions[transaction]
                if type(midl_result) == dict:
                    for key_dict in midl_result.keys():
                        if type(midl_result[key_dict]) == dict:
                            list_value.append(midl_result[key_dict].get('code'))
                            if midl_result[key_dict].get('code') == currency:
                                yield transactions
    if currency not in list_value:
        yield "Данной валюты нет в списке транзакций"


def transaction_description(list_transactions: list[dict]) -> Iterator[str]:
    """Функция генератор, принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""

    for transactions in list_transactions:
        yield transactions.get('description')


def card_number_generator(start: int, end: int) -> str:
    """Функция генератор, выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров."""

    if start < 1:
        return "Введено некорректное значение для генерации номера карты"

    elif end > 9999999999999999:
        return "Введено некорректное значение для генерации номера карты"

    elif start > end:
        return "Введено некорректное значение для генерации номера карты"

    else:
        list = [str(x).zfill(16)[:4] + ' ' + str(x).zfill(16)[4:8] + ' ' + str(x).zfill(16)[8:12] + ' ' + str(x).zfill(16)[12:] for x in range(start, end + 1)]
        return list
