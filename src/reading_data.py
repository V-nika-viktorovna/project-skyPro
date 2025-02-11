import csv

import pandas as pd


def get_data_from_csv(way_file: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV.
    Принимает путь к файлу CSV в качестве аргумента, в строчном формате.
    Возвращает список словарей с транзакциями.
    При невозможности считать файл выдает сообщение об ошибке."""

    try:
        with open(way_file) as file:
            reader_data_csv = csv.DictReader(file, delimiter=';')
            result = []
            for data in reader_data_csv:
                result.append(data)
        return result
    except Exception as e:
        return f'Ошибка: {e}'


def get_data_from_excel(way_file: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel.
        Принимает путь к файлу Excel в качестве аргумента, в строчном формате.
        Возвращает список словарей с транзакциями.
        При невозможности считать файл выдает сообщение об ошибке."""

    try:
        reader_data_excel = pd.read_excel(way_file)

        result = []
        count = 0
        for _ in range(len(reader_data_excel)):
            data_dict = {
                            'id': float(reader_data_excel.iloc[count]['id']),
                            'state': reader_data_excel.iloc[count]['state'],
                            'date': reader_data_excel.iloc[count]['date'],
                            'amount': float(reader_data_excel.iloc[count]['amount']),
                            'currency_name': reader_data_excel.iloc[count]['currency_name'],
                            'currency_code': reader_data_excel.iloc[count]['currency_code'],
                            'from': reader_data_excel.iloc[count]['from'],
                            'to': reader_data_excel.iloc[count]['to'],
                            'description': reader_data_excel.iloc[count]['description']
            }
            result.append(data_dict)
            count += 1
        return result

    except Exception as e:
        return f'Ошибка: {e}'


if __name__ == '__main__':
    print(get_data_from_csv('C:/Users/PROGRAMM/Downloads'))
    print(get_data_from_excel('C:/Users/PROGRAMM/Downloads/transactions_excel.xlsx'))
