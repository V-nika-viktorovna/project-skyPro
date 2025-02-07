import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
logger_hendler = logging.FileHandler('C:/Users/PROGRAMM/PycharmProjects/work/logs/utils.log', 'w')
logger_formater = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
logger_hendler.setFormatter(logger_formater)
logger.addHandler(logger_hendler)


def get_data_json(way_file="") -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    data = []
    try:
        logger.info('Open and read the file with transactions')
        with open(way_file, encoding='utf-8') as file:
            data = json.load(file)
        logger.info('Transactions were read successfully')
    except Exception as e:
        logger.error(f'error: {e}')
        return data
    finally:
        return data


if __name__ == '__main__':
    get_data_json('C:/Users/PROGRAMM/PycharmProjects/work/data/operation.json')
