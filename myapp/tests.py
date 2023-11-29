import unittest
from unittest.mock import MagicMock
from .management.commands.run_telegram_bot import start, games, handle_help, handle_add_game, echo_all


class TestBot(unittest.TestCase):

    def test_start(self):
        message = MagicMock()
        message.chat.id = 846935339
        start(message)

    def test_help(self):
        message = MagicMock()
        message.chat.id = 846935339
        handle_help(message)

    def test_figures(self):
        message = MagicMock()
        message.chat.id = 846935339
        games(message)

    def test_add_figure(self):
        message = MagicMock()
        message.chat.id = 846935339
        handle_add_game(message)


if __name__ == '__main__':
    unittest.main()