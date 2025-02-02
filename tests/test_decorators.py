from src.decorators import log


def test_decorator_log_try_file_name_not_set():
    @log()
    def summ_num(x, y):
        return x + y

    a = summ_num(8, 9)
    assert a == 'summ_num ok'


def test_decorator_log_try_file_name_given_console_output(capsys):
    @log('mylog.txt')
    def summ_num(x, y):
        return x + y

    print(summ_num(8, 9))
    text_file = open('mylog.txt', 'r')
    text = text_file.read()
    captured = capsys.readouterr()
    assert captured.out == '\n'
    assert text == 'summ_num ok'


def test_decorator_log_error(capsys):
    @log()
    def summ_num(x, y):
        return x + y

    print(summ_num(8, 'fhgf'))
    captured = capsys.readouterr()
    assert captured.out == "summ_num error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (8, 'fhgf'), {} \n"
