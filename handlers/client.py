from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboard import kb_client
from aiogram.types import ReplyKeyboardRemove
from qcf.global_fr import ozgarmas_buyruqlarni_saralash
from qcf.global_or import *


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    message = message
    try:
        print(121222222222222222222222222)
        await bot.send_message(message.from_user.id, "Yoqimlik ishtaxa!", reply_markup=kb_client)
    except:
        # await message.delete()
        await message.reply("Botning shaxsiy sahifasiga yozing:\nhttps://t.me/Pitsanariya_bot")


# @dp.message_handler(commands=['ish_vaqti'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.chat.id, "Du-Sha: 08:30 dan 23:30 gacha", reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['joylashuv'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Mirabad avinew 20 uy')


def register_handler_client(dpr: Dispatcher):
    print(BUYRUQLAR['start'], BUYRUQLAR['help'])
    print([*BUYRUQLAR['start'], *BUYRUQLAR['help']])
    dpr.register_message_handler(command_start,
                                 lambda m: ozgarmas_buyruqlarni_saralash(m) in [*BUYRUQLAR['start'], *BUYRUQLAR['help']])
    dpr.register_message_handler(pizza_open_command, commands=['ish_vaqti'])
    dpr.register_message_handler(pizza_place_command, commands=['joylashuv'])


