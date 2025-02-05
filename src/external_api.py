import datetime
import os

import requests
from dotenv import load_dotenv


def get_transaction_amount_rub(transaction={}) -> str:
    """функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    Для конвертации валюты используется Exchange Rates Data API: https://apilayer.com/exchangerates_data-api."""
    try:
        result_amount = float(transaction.get('operationAmount').get('amount'))
    except AttributeError:
        return "Транзакций не найдено"
    else:
        load_dotenv()
        api_key = os.getenv('API_KEY')
        headers = {"apikey": api_key}
        date_obj = datetime.datetime.now()
        date_year = date_obj.strftime("%Y")
        date_month = date_obj.strftime("%m")
        date_day = date_obj.strftime("%d")
        if transaction.get('operationAmount').get('currency').get('code') != "RUB":
            if transaction.get('operationAmount').get('currency').get('code') == "USD":
                restone = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={result_amount}&date={date_year}-{date_month}-{date_day}', headers)
                result_amount = restone.json().get('result')
                return f'{round(result_amount, 2)} RUB'
            elif transaction.get('operationAmount').get('currency').get('code') == "EUR":
                restone = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={result_amount}&date={date_year}-{date_month}-{date_day}', headers)
                result_amount = restone.json().get('result')
                return f'{round(result_amount, 2)} RUB'
            else:
                return f"{result_amount} {transaction.get('operationAmount').get('currency').get('code')}, данная валюта не конвертируется"
        else:
            return f"{result_amount} RUB"
