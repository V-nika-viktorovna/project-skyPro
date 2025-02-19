import unittest.mock
from unittest.mock import patch

from src.main import main


class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'CANCELED', 'нет', 'да', 'да', 'орган'])
    def test_main_try_json(self, mock_input):
        main()
        mock_input.assert_called()

    @patch('builtins.input', side_effect=['2', 'CANCELED', 'нет', 'да', 'да', 'счет'])
    def test_main_try_csv_none(self, mock_input):
        main()
        mock_input.assert_called()

    @patch('builtins.input', side_effect=['2', 'CANCELED', 'нет', 'да', '', ''])
    def test_main_try_csv(self, mock_input):
        main()
        mock_input.assert_called()

    @patch('builtins.input', side_effect=['3', 'CANCELED', 'да', 'по возрастанию', '', ''])
    def test_main_try_exlx(self, mock_input):
        main()
        mock_input.assert_called()
