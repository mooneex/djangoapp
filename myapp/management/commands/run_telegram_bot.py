from django.core.management.base import BaseCommand
import telebot
from telebot import types
from myapp. import Game


bot = telebot.TeleBot("6767763518:AAHpwumvSlKIP3rLIDbs5zlMISem0vqby_g")  # Вставьте сюда свой токен


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['games'])
def games(message):
    games = Game.objects.all()
    for game in games:
        bot.send_message(message.chat.id, f"game: {game.name}, rank: {game.rank}")


response = (
    "Commands:\n"
    "/start: type start to get Hello World!\n"
    "/games: show games\n"
    "/add <game> <rank>: add another Game"
)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, response)


@bot.message_handler(commands=['add'])
def handle_add_game(message):
    parts = message.text.split(maxsplit=2)
    if len(parts) == 3:
        _, name, rank = parts
        game = Game.objects.create(name=name, rank=rank)
        bot.send_message(message.chat.id, f"game {name}, rank {rank} added!")
    else:
        bot.send_message(message.chat.id, "Используйте /add <game> <rank>")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")


