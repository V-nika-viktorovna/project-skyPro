import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
logger_hendler = logging.FileHandler('C:/Users/PROGRAMM/PycharmProjects/work/logs/masks.log', 'w')
logger_formater = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
logger_hendler.setFormatter(logger_formater)
logger.addHandler(logger_hendler)


def get_mask_card_numder(number_card: str) -> str:
    """Функция принимает номер карты и возвращает строку с ее маской"""

    logger.info('Checking the correctness of the card number')
    if isinstance(number_card, str):
        if not number_card.isdigit():
            logger.error('Format error')
            return "Номер карты не может содержать буквы!"

        if len(number_card) != 16:
            logger.error('Number length error')
            return "Вы ввели некорректный номер карты!"
        else:
            logger.info('Creating a card number mask')
            return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    else:
        return 'Введите номер в строчном формате'


def get_mask_account(number_account: str) -> str:
    """Функция принимает номер счета и возвращает строку с его маской"""

    logger.info('Checking the correctness of the account number')
    if isinstance(number_account, str):
        if not number_account.isdigit():
            logger.error('Number length error')
            return "Номер счета не может содержать буквы!"

        if len(number_account) != 20:
            logger.error('Number length error')
            return "Вы ввели некорректный номер счета!"
        else:
            logger.info('Create an account number mask')
            return f"**{number_account[-4:]}"
    else:
        return 'Введите номер в строчном формате'


if __name__ == '__main__':
    print(get_mask_card_numder('123456789123456'))
    print(get_mask_account('12345678912345678912'))
