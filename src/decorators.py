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
            except Exception as e:
                result = f'{name_func} error: {e}. Inputs: {args}, {kwargs} '
                return result
            else:
                result = f'{name_func} ok'
                return result
            finally:
                if filename:
                    with open(filename, 'w') as file:
                        file.write(result)
                    return try_func

        return wrapper
    return inner



@log()
def summ_num(x, y):
    return x + y

print(summ_num(8, 'fhgf'))
