from telebot import *
from json import dump, load
from config import error, info


BOTS_ = {
    "Test": "724876434:AAG2Cp51nhI8T5Vm4TyWVG0bC7zUETJI5vE",
}

def bot_init(token, name="noName"):
    BOTS_[name.get()] = token.get()
    info("Бот был успешно добавлен / изменен. Можете закрыть окно или изменить добавленого вами бота")
    print(BOTS_)  

def choose(name):
    print(name)