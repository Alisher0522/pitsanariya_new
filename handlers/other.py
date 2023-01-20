from aiogram import types, Dispatcher
from create_bot import bot, dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    print(message.chat.id, message.chat.values)
    print(message.from_user.values)
    user_id = message.from_user.id
    is_member = await message.chat.get_member(user_id)
    print(is_member, 121111, message.text)
    # await message.answer(message.text)
    await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


def register_handler_other(dpr: Dispatcher):
    dpr.register_message_handler(echo_send)
