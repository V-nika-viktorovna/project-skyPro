import os.path

from src.filter_transactions import filter_transactions_by_description
from src.processing import filter_by_state, sort_by_date
from src.reading_data import get_data_from_csv, get_data_from_excel
from src.utils import get_data_json
from src.widget import get_date, mask_account_card


def main():
    """Функция отвечает за основную логику проекта и связывает функциональности между собой."""

    CURRENT_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')

    print('Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n\
           Выберите необходимый пункт меню:\n\
            1. Получить информацию о транзакциях из JSON-файла\n\
            2. Получить информацию о транзакциях из CSV-файла\n\
            3. Получить информацию о транзакциях из XLSX-файла')

    input_flag_1 = True
    while input_flag_1:
        select_file = input('Пользователь:')
        if select_file:
            select_file = int(select_file)
            if select_file in [1, 2, 3]:
                index_file = select_file - 1
                list_file = ['JSON-файл', 'CSV-файл', 'XLSX-файл']
                print(f'Для обработки выбран {list_file[index_file]}')
                input_flag_1 = False
            else:
                print('Вы выбрали не существующий пункт!\nВыберите необходимый пункт меню:\n\
                    1. Получить информацию о транзакциях из JSON-файла\n\
                    2. Получить информацию о транзакциях из CSV-файла\n\
                    3. Получить информацию о транзакциях из XLSX-файла')
        else:
            print('Вы выбрали не существующий пункт!\nВыберите необходимый пункт меню:\n\
                1. Получить информацию о транзакциях из JSON-файла\n\
                2. Получить информацию о транзакциях из CSV-файла\n\
                3. Получить информацию о транзакциях из XLSX-файла')

    print('Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n\
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

    input_flag_2 = True
    while input_flag_2:
        select_state = input('Пользователь:')
        select_state = select_state.upper()
        if select_state in ['EXECUTED', 'CANCELED', 'PENDING']:
            input_flag_2 = False
            print(f'Программа: Операции отфильтрованы по статусу "{select_state}"')
        else:
            print('Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n\
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

    select_date = input('Программа: Отсортировать операции по дате? Да/Нет\nПользователь:')
    select_date = select_date.lower()
    sorting_direction = ''
    print(f'вы ввели {select_date}')
    if select_date == ('да'):
        sorting_direction = input('Программа: Отсортировать "по возрастанию" или "по убыванию"?\nПользователь:')
        sorting_direction = sorting_direction.lower()
        if sorting_direction not in ['по возрастанию', 'по убыванию']:
            print('К сожалению введенные данные не распознаны, установлено значение "по убыванию"')
            sorting_direction = 'по убыванию'
    if select_date not in ['да', 'нет']:
        sorting_direction = 'по убыванию'

    select_currency = input('Программа: Выводить только рублевые тразакции? Да/Нет\nПользователь:')
    select_currency = select_currency.lower()
    if select_currency not in ['да', 'нет']:
        select_currency = 'нет'
    print(f'вы выбрали {select_currency} для рублевых тразакций')

    select_filter = input('Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь:')
    select_filter = select_filter.lower()
    print(f'вы выбрали {select_filter} для ыильтрации тразакций')
    if select_filter not in ['да', 'нет']:
        select_filter = 'нет'
    if select_filter == 'нет':
        print('слово для фильтрации не задано!')
    filtration_word = ''
    if select_filter == 'да':
        filtration_word = input('Введите слово для фильтрации транзакций\nПользователь:')
        filtration_word = filtration_word.lower()
        print(f'слово для фильтрации: {filtration_word}')
    print('Программа: Распечатываю итоговый список транзакций...')

    if select_file == 1:

        json_file = os.path.join(DATA_DIR, 'operations.json')
        read_json_file = get_data_json(json_file)

        get_filter_state = filter_by_state(read_json_file, select_state)
        if sorting_direction == 'по возрастанию':
            sort_flag = False
        else:
            sort_flag = True
        get_filter_state_date = sort_by_date(get_filter_state, sort_flag)
        if select_currency == 'да':
            filter_transaction = []
            for transaction in get_filter_state_date:
                if transaction.get('operationAmount').get('currency').get('code') == "RUB":
                    filter_transaction.append(transaction)
        else:
            filter_transaction = get_filter_state_date
        filter_transaction_by_word = filter_transactions_by_description(filter_transaction, filtration_word)

        if filter_transaction_by_word != 'Операции не найдены':
            print(f'\n\
    Всего банковских операций в выборке:{len(filter_transaction_by_word)}')
            for filter_dict in filter_transaction_by_word:
                from_transaction = mask_account_card(filter_dict.get('from'))
                if not from_transaction:
                    from_transaction = 'Номер карты или счета не задан'
                to_transaction = mask_account_card(filter_dict.get('to'))
                if not to_transaction:
                    to_transaction = 'Номер карты или счета не задан'
                print(f'\n\
    {get_date(filter_dict.get('date'))} {filter_dict.get('description')}\n\
    {from_transaction}->{to_transaction}\n\
    Сумма: {filter_dict.get('operationAmount').get('amount')} {filter_dict.get('operationAmount').get('currency').get('code')}')
        else:
            print('По вашему запросу транзакций не найдено!')

    elif select_file == 2:
        print('здесь')
        csv_file = os.path.join(DATA_DIR, 'transactions.csv')
        read_csv_file = get_data_from_csv(csv_file)
        get_filter_state = filter_by_state(read_csv_file, select_state)
        if sorting_direction == 'по возрастанию':
            sort_flag = False
        else:
            sort_flag = True
        get_filter_state_date = sort_by_date(get_filter_state, sort_flag)
        if select_currency == 'да':
            filter_transaction = []
            for transaction in get_filter_state_date:
                if transaction.get('currency_code') == "RUB":
                    filter_transaction.append(transaction)
        else:
            filter_transaction = get_filter_state_date

        filter_transaction_by_word = filter_transactions_by_description(filter_transaction, filtration_word)

        if filter_transaction_by_word != 'Операции не найдены':
            print(f'\n\
    Всего банковских операций в выборке:{len(filter_transaction_by_word)}')
            for filter_dict in filter_transaction_by_word:
                from_transaction = mask_account_card(filter_dict.get('from'))
                if not from_transaction:
                    from_transaction = 'Номер карты или счета не задан'
                to_transaction = mask_account_card(filter_dict.get('to'))
                if not to_transaction:
                    to_transaction = 'Номер карты или счета не задан'
                print(f'\n\
    {get_date(filter_dict.get('date'))} {filter_dict.get('description')}\n\
    {from_transaction}->{to_transaction}\n\
    Сумма: {filter_dict.get('amount')} {filter_dict.get('currency_code')}')
        else:
            print('По вашему запросу транзакций не найдено!')

    elif select_file == 3:

        excel_file = os.path.join(DATA_DIR, 'transactions_excel.xlsx')
        read_csv_file = get_data_from_excel(excel_file)

        get_filter_state = filter_by_state(read_csv_file, select_state)
        if sorting_direction == 'по возрастанию':
            sort_flag = False
        else:
            sort_flag = True
        get_filter_state_date = sort_by_date(get_filter_state, sort_flag)
        if select_currency == 'да':
            filter_transaction = []
            for transaction in get_filter_state_date:
                if transaction.get('currency_code') == "RUB":
                    filter_transaction.append(transaction)
        else:
            filter_transaction = get_filter_state_date
        filter_transaction_by_word = filter_transactions_by_description(filter_transaction, filtration_word)

        if filter_transaction_by_word != 'Операции не найдены':
            print(f'\n\
        Всего банковских операций в выборке:{len(filter_transaction_by_word)}')
            for filter_dict in filter_transaction_by_word:
                from_transaction = mask_account_card(filter_dict.get('from'))
                if not from_transaction:
                    from_transaction = 'Номер карты или счета не задан'
                to_transaction = mask_account_card(filter_dict.get('to'))
                if not to_transaction:
                    to_transaction = 'Номер карты или счета не задан'
                print(f'\n\
        {get_date(filter_dict.get('date'))} {filter_dict.get('description')}\n\
        {from_transaction}->{to_transaction}\n\
        Сумма: {filter_dict.get('amount')} {filter_dict.get('currency_code')}')
        else:
            print('По вашему запросу транзакций не найдено!')
