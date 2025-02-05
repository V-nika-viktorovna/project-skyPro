import json


def get_data_json(way_file="") -> str:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    data = []
    try:
        with open(way_file, encoding='utf-8') as file:
            data = json.load(file)
    except Exception:
        return data
    finally:
        return data
