from aiogram import types
from PsychoTests.misc import bot, dp, tests_buttons, tests_names_buttons
import PsychoTests.database as database
from PsychoTests.config import HOW_MANY_QUESTIONS


async def finnaly(m: types.Message):
    await bot.send_message(m.from_user.id, "Поздравляем, вы прошли тест!")
    if database.get_test_result(m.from_user.id, "how_many") <= 50:
        await bot.send_message(m.from_user.id, "У вас низкий уровень беспокойства!")
    elif database.get_test_result(m.from_user.id, "how_many") <= 65:
        await bot.send_message(m.from_user.id, "У вас средний уровень беспокойства!")
    elif database.get_test_result(m.from_user.id, "how_many") > 65:
        await bot.send_message(m.from_user.id, "У у вас хроническое беспокойство!")
    await bot.send_message(m.from_user.id, reply_markup = tests_buttons("", return_out_only = True))


@dp.callback_query_handler(lambda c: c.data == "how_many")
async def how_many_start(m: types.Message):
    await bot.send_message(m.from_user.id, ("В каждом вопросе поставьте то число, которое наилучшим образом описывает вас:\n"
                                       "Варианты ответов:\n"
                                       "Это вообще не обо мне/не про меня\n"
                                       "Немного на меня похоже\n"
                                       "Да, это похоже на меня\n"
                                       "Это очень на меня похоже,\n"
                                       "Это точно про меня/обо мне"))
    await bot.send_message(m.from_user.id,
                           HOW_MANY_QUESTIONS[database.get_test_state(m.from_user.id, "how_many")],
                           reply_markup = tests_buttons("how_many"))

@dp.callback_query_handler(lambda c: c.data == "how_many_not_me")
async def how_many_not_me(m: types.Message):
    try:
        if database.get_test_state(m.from_user.id, "how_many") in [3, 8, 10, 11]:
            database.update_test(m.from_user.id, "how_many", 5)
        else:
            database.update_test(m.from_user.id, "how_many", 1)
        await bot.send_message(m.from_user.id,
                               HOW_MANY_QUESTIONS[database.get_test_state(m.from_user.id, "how_many")],
                               reply_markup=tests_buttons("how_many"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: c.data == "how_many_low")
async def how_many_low(m: types.Message):
    try:
        if database.get_test_state(m.from_user.id, "how_many") in [3, 8, 10, 11]:
            database.update_test(m.from_user.id, "how_many", 4)
        else:
            database.update_test(m.from_user.id, "how_many", 2)
        await bot.send_message(m.from_user.id,
                               HOW_MANY_QUESTIONS[database.get_test_state(m.from_user.id, "how_many")],
                               reply_markup=tests_buttons("how_many"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: c.data == "how_many_middle")
async def how_many_middle(m: types.Message):
    try:
        database.update_test(m.from_user.id, "how_many", 3)
        await bot.send_message(m.from_user.id,
                               HOW_MANY_QUESTIONS[database.get_test_state(m.from_user.id, "how_many")],
                               reply_markup=tests_buttons("how_many"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: c.data == "how_many_very")
async def how_many_very(m: types.Message):
    try:
        if database.get_test_state(m.from_user.id, "how_many") in [3, 8, 10, 11]:
            database.update_test(m.from_user.id, "how_many", 2)
        else:
            database.update_test(m.from_user.id, "how_many", 4)
        await bot.send_message(m.from_user.id,
                               HOW_MANY_QUESTIONS[database.get_test_state(m.from_user.id, "how_many")],
                               reply_markup=tests_buttons("how_many"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: c.data == "how_many_me")
async def how_many_me(m: types.Message):
    try:
        if database.get_test_state(m.from_user.id, "how_many") in [3, 8, 10, 11]:
            database.update_test(m.from_user.id, "how_many", 1)
        else:
            database.update_test(m.from_user.id, "how_many", 5)
        await bot.send_message(m.from_user.id,
                               HOW_MANY_QUESTIONS[database.get_test_state(m.from_user.id, "how_many")],
                               reply_markup=tests_buttons("how_many"))
    except Exception as e:
        print(e)
        await finnaly(m)


@dp.callback_query_handler(lambda c: (c.data == "uncertainty_out") or (c.data == "out"))
async def hm_out(m: types.Message):
    await bot.send_message(m.chat.id, "Нет такого человека, который бы беспокоился обо всем. Кого-то из нас больше "
                                      "всего заставляют беспокоиться отношения, кто-то беспокоится чаще из-за "
                                      "финансовой ситуации, кто-то по поводу здоровья.  У каждого из нас существует "
                                      "свой уникальный профиль того, почему и как мы беспокоимся. Ниже представлены "
                                      "пять опросников, которые помогут вам составить ваш личный профиль "
                                      "беспокойства. А полученный профиль в свою очередь поможет вам понять на чем "
                                      "именно вам нужно сфокусироваться, чтобы сделать вашу жизнь более комфортной и "
                                      "гармоничной.")
    await bot.send_message(m.chat.id, "Выберите интересующий вас тест:", reply_markup=tests_names_buttons())