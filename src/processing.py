def filter_by_state(get_list_dict: list[dict], state="EXECUTED") -> list[dict]:
    """Принимает список словарей и опционально значение для ключа state, по умолсанию
    значение данного ключа EXECUTED.
    Возвращает список словарей, у которых ключа state соответствует искомому"""

    up_list_dict = []
    if isinstance(get_list_dict, list):
        for get_dict in get_list_dict:
            for key_dict in get_dict.keys():
                if get_dict[key_dict] == state:
                    up_list_dict.append(get_dict)
        return up_list_dict
    else:
        return "Введенное значение не является списком!"


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
