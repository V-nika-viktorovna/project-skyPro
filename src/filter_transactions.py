import re
from collections import Counter

from src.reading_data import get_data_from_csv


def filter_transactions_by_description(transactions_list=list[dict], search_bar='') -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка.
    Если операции с данной строкой не найдены, то возвращается сообщение об этом """

    result = []
    search_compile = re.compile(search_bar)
    try:
        for dict_transaction in transactions_list:
            matches = search_compile.search(dict_transaction.get('description'))
            if matches:
                result.append(dict_transaction)

    except Exception as e:
        result = f'Ошибка: {e}'

    finally:
        if result:
            return result
        return 'Операции не найдены'


def filter_transactions_counter_description(transactions_list=list[dict], category_list=list[str]) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории
    Если операции с данными категориями не найдены, то возвращается сообщение об этом"""

    list_value_description = []
    try:
        for dict_transaction in transactions_list:
            if dict_transaction.get('description') in category_list:
                list_value_description.append(dict_transaction.get('description'))
        result = dict(Counter(list_value_description))

    except Exception as e:
        result = f'Ошибка: {e}'

    finally:
        if result:
            return result
        return 'Операции не найдены'


if __name__ == '__main__':

    try_func = get_data_from_csv('C:/Users/PROGRAMM/Downloads/transactions.csv')
    print(filter_transactions_by_description(try_func))
