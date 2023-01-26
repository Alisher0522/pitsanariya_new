from aiogram import types, Dispatcher
from aiogram.types import ContentType

from create_bot import bot, dp


@dp.message_handler(content_types=ContentType.CONTACT)
async def process_contact(message: types.Message):
    contact = message.contact
    answer = f"Salom {contact.first_name}\nnomer uchun sps: {contact.phone_number}"
    await message.reply(answer)
countr = 0
# @dp.message_handler()
async def echo_send(message: types.Message):
    global countr
    chat_id = message.chat.id
    print(message.chat.id, message.chat.values)
    print(message.from_user.is_bot)
    user_id = message.from_user.id
    is_member = await message.chat.get_member(user_id)
    # print(is_member, 121111, message.text)
    # await message.answer(message.text)
    sender_chat = message.sender_chat
    print(message.values, 3131313131)
    countr += 1
    if sender_chat.type == "channel":
        if countr <= 2:
            chat_id = sender_chat.id
            print(chat_id)
            await bot.send_message(chat_id, "а и б сидели на трубе а упал б пропал что осталось на трубе?")
        else:
            await message.reply(message.text)
    else:
        await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


def register_handler_other(dpr: Dispatcher):
    dpr.register_message_handler(echo_send)
