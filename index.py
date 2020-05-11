from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import executor, types
from data.misc import dp, bot, tests_names_buttons
from data import tests
from data import database



@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    database.create_new_user(m.from_user.id)
    await bot.send_message(m.chat.id, "Нет такого человека, который бы беспокоился обо всем. Кого-то из нас больше "
                                      "всего заставляют беспокоиться отношения, кто-то беспокоится чаще из-за "
                                      "финансовой ситуации, кто-то по поводу здоровья.  У каждого из нас существует "
                                      "свой уникальный профиль того, почему и как мы беспокоимся. Ниже представлены "
                                      "пять опросников, которые помогут вам составить ваш личный профиль "
                                      "беспокойства. А полученный профиль в свою очередь поможет вам понять на чем "
                                      "именно вам нужно сфокусироваться, чтобы сделать вашу жизнь более комфортной и "
                                      "гармоничной.")
    await bot.send_message(m.chat.id, "Выберите интересующий вас тест:", reply_markup=tests_names_buttons())

print(__name__)

if __name__ == "__main__":
    print("exe!!!!!!!!!!!")
    executor.start_polling(dp)
