from aiogram.dispatcher.webhook import EditMessageText
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from emoji import emojize
b1 = KeyboardButton("/ish_vaqti")
b2 = KeyboardButton('/joylashuv')
b3 = KeyboardButton(emojize(":pizza: Menu"))
b4 = KeyboardButton("Nomerni jo'natish", request_contact=True)
b5 = KeyboardButton("Joylashuvni yuborish", request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).insert(b3).add(b4).add(b5)