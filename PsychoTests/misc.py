from aiogram import Bot, Dispatcher, types
import config
bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

from config import TESTS_NAMES
from config import TESTS_BUTTONS


def tests_names_buttons():
    btns = []
    for k, i in TESTS_NAMES.items():
        btns.append(types.InlineKeyboardButton(i, callback_data=k))
    keyboard = types.InlineKeyboardMarkup(row_width=1).add(*btns)
    return keyboard


def tests_buttons(test_name, return_out_only = False):
    btns = []
    for k, i in TESTS_BUTTONS.items():
        btns.append(types.InlineKeyboardButton(i, callback_data=test_name + "_" + k))
    keyboard = types.InlineKeyboardMarkup(row_width=1).add(*btns)
    if return_out_only:
        return types.InlineKeyboardMarkup(types.InlineKeyboardButton("Выйти из теста", callback_data="out"))
    return keyboard