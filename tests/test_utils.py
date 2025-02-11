import json
import os.path

from src.utils import get_data_json, CURRENT_DIR


def test_get_data_json_try():
    with open('C:/Users/PROGRAMM/PycharmProjects/work/data/operations.json', encoding='utf-8') as file:
        data = json.load(file)
    assert get_data_json('C:/Users/PROGRAMM/PycharmProjects/work/data/operations.json') == data


def test_get_data_json_none():
    assert get_data_json() == []


def test_get_data_json_out_file():
    assert get_data_json('C:/Users/PROGRAMM/PycharmProjects/work/data/way.txt') == []


def test_get_data_json_mystery_file():
    assert get_data_json('C:/Users/PROGRAMM/PycharmProjects/work/data/') == []
