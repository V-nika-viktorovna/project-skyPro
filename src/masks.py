def get_mask_card_numder(number_card: str) -> str:
    """Функция принимает номер карты и возвращает строку с ее маской"""

    if isinstance(number_card, str):
        if not number_card.isdigit():
            return "Номер карты не может содержать буквы!"

        if len(number_card) != 16:
            return "Вы ввели некорректный номер карты!"
        else:
            return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    else:
        return 'Введите номер в строчном формате'


def get_mask_account(number_account: str) -> str:
    """Функция принимает номер счета и возвращает строку с его маской"""

    if isinstance(number_account, str):
        if not number_account.isdigit():
            return "Номер счета не может содержать буквы!"

        if len(number_account) != 20:
            return "Вы ввели некорректный номер счета!"
        else:
            return f"**{number_account[-4:]}"
    else:
        return 'Введите номер в строчном формате'
