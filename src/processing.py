def filter_by_state(get_list_dict: list[dict], state="EXECUTED") -> list[dict]:
    """Принимает список словарей и опционально значение для ключа state, по умолсанию
    значение данного ключа EXECUTED.
    Возвращает список словарей, у которых ключа state соответствует искомому"""

    up_list_dict = []

    for get_dict in get_list_dict:
        for key_dict in get_dict.keys():
            if get_dict[key_dict] == state:
                up_list_dict.append(get_dict)
    return up_list_dict


def sort_by_date(get_list_dict: list[dict], ascending=True) -> list[dict]:
    """Принимает список словарей и опционально параметр порядка сортировки.
    Возвращает список отсортированный по дате"""

    up_list_dict = []
    if ascending:
        for get_dict in get_list_dict:
            up_list_dict = sorted(get_list_dict, key=lambda x: x.get("date"), reverse=True)
        return up_list_dict
    else:
        for get_dict in get_list_dict:
            up_list_dict = sorted(get_list_dict, key=lambda x: x.get("date"))
        return up_list_dict


if __name__ == '__main__':
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
