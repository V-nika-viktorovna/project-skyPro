from functools import wraps


def log(filename='') -> str:
    """Декоратор, который логирует выполнения функции, а также ее результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль.
    Логированиевключает:
    Имя функции и результат выполнения при успешной операции.
    Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке."""

    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name_func = func.__name__
            try:
                try_func = func(*args, **kwargs)
                result = 'ok'
                return try_func
            except Exception as e:
                result = f'error: {e}. Inputs: {args}, {kwargs} '
            finally:
                if filename:
                    text_file = open(filename, 'w')
                    result_decor = f'{name_func} {result}'
                    text_file.write(result_decor)
                    text_file.close()
                    return ""
                else:
                    result_decor = f'{name_func} {result}'
                    return result_decor

        return wrapper
    return inner
