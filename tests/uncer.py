from aiogram import types
from data.misc import bot, dp, tests_buttons, tests_names_buttons
import data.database as database
from data.config import UNCERTAINTY_QUESTIONS


async def finnaly(m: types.Message):
    await bot.send_message(m.from_user.id, "Поздравляем, вы прошли тест!")
    if database.get_test_result(m.from_user.id, "how_many") <= 40:
        await bot.send_message(m.from_user.id, "Вы способны достаточно неплохо справляться с неопределенностью!")
    elif database.get_test_result(m.from_user.id, "how_many") <= 65:
        await bot.send_message(m.from_user.id, "У вас есть сложности с перенесением неопределенности!")
    elif database.get_test_result(m.from_user.id, "how_many") > 75:
        await bot.send_message(m.from_user.id, "Есть генерализованное тревожное расстройство!")


@dp.callback_query_handler(lambda c: c.data == "uncertainty")
async def how_many_start(m: types.Message):
    await bot.send_message(m.from_user.id, ("В каждом вопросе поставьте то число, которое наилучшим образом описывает вас:\n"
                                       "Варианты ответов:\n"
                                       "Это вообще не обо мне/не про меня\n"
                                       "Немного на меня похоже\n"
                                       "Да, это похоже на меня\n"
                                       "Это очень на меня похоже,\n"
                                       "Это точно про меня/обо мне"))
    await bot.send_message(m.from_user.id,
                           UNCERTAINTY_QUESTIONS[database.get_test_state(m.from_user.id, "uncertainty")],
                           reply_markup = tests_buttons("uncertainty"))

@dp.callback_query_handler(lambda c: c.data == "uncertainty_not_me")
async def how_many_not_me(m: types.Message):
    try:
        database.update_test(m.from_user.id, "uncertainty", 1)
        await bot.send_message(m.from_user.id,
                               UNCERTAINTY_QUESTIONS[database.get_test_state(m.from_user.id, "uncertainty")],
                               reply_markup=tests_buttons("uncertainty"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: c.data == "uncertainty_low")
async def how_many_low(m: types.Message):
    try:
        database.update_test(m.from_user.id, "uncertainty", 2)
        await bot.send_message(m.from_user.id,
                               UNCERTAINTY_QUESTIONS[database.get_test_state(m.from_user.id, "uncertainty")],
                               reply_markup=tests_buttons("uncertainty"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: c.data == "uncertainty_middle")
async def how_many_middle(m: types.Message):
    try:
        database.update_test(m.from_user.id, "uncertainty", 3)
        await bot.send_message(m.from_user.id,
                               UNCERTAINTY_QUESTIONS[database.get_test_state(m.from_user.id, "uncertainty")],
                               reply_markup=tests_buttons("uncertainty"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: c.data == "uncertainty_very")
async def how_many_very(m: types.Message):
    try:
        database.update_test(m.from_user.id, "uncertainty", 4)
        await bot.send_message(m.from_user.id,
                               UNCERTAINTY_QUESTIONS[database.get_test_state(m.from_user.id, "uncertainty")],
                               reply_markup=tests_buttons("uncertainty"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: c.data == "uncertainty_me")
async def how_many_me(m: types.Message):
    try:
        database.update_test(m.from_user.id, "uncertainty", 5)
        await bot.send_message(m.from_user.id,
                               UNCERTAINTY_QUESTIONS[database.get_test_state(m.from_user.id, "uncertainty")],
                               reply_markup=tests_buttons("uncertainty"))
    except Exception as e:
        print(e)
        await finnaly(m)

@dp.callback_query_handler(lambda c: (c.data == "uncertainty_out") or (c.data == "out"))
async def u_out(m: types.Message):
    await bot.send_message(m.chat.id, "Нет такого человека, который бы беспокоился обо всем. Кого-то из нас больше "
                                      "всего заставляют беспокоиться отношения, кто-то беспокоится чаще из-за "
                                      "финансовой ситуации, кто-то по поводу здоровья.  У каждого из нас существует "
                                      "свой уникальный профиль того, почему и как мы беспокоимся. Ниже представлены "
                                      "пять опросников, которые помогут вам составить ваш личный профиль "
                                      "беспокойства. А полученный профиль в свою очередь поможет вам понять на чем "
                                      "именно вам нужно сфокусироваться, чтобы сделать вашу жизнь более комфортной и "
                                      "гармоничной.")
    await bot.send_message(m.chat.id, "Выберите интересующий вас тест:", reply_markup=tests_names_buttons())
