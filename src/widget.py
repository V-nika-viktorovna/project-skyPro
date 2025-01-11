from src.masks import get_mask_card_numder, get_mask_account


def mask_account_card():
    """Принимает от пользователя тип и номер карты или счета
    и выводит их маску"""

    account_card = input("Введите тип и номер карты или счета:")
    card = []
    account = []
    card_str = ''
    for index in account_card:
        if index.isdigit():
            card.append(index)
            card_str = ''.join(card)
        else:
            account.append(index)

    if len(card_str) == 16:
        return f"{''.join(account)} {get_mask_card_numder(card_str)}"
    elif len(card_str) == 20:
        return f"{''.join(account)} {get_mask_account(card_str)}"
    else:
        return "Вы ввели некоректный номер карты или счета"


def get_date(date: str) -> str:
    """Функция принимает дату в глобальном формате и
     дату в формате ДД.ММ.ГГГГ"""

    if date[4] != "-" or date[7] != "-":
        return " Неверный формат даты"
    else:
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


if __name__ == '__main__':
    print(mask_account_card())
