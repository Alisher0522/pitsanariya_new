from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
import os

# Create a bot instance
bot = Bot(token='5814262335:AAHMx5RNc-Y-GsUFJFnLh0O7SA480urAp7M')
dp = Dispatcher(bot)

# Define a command handler for the '/info' command
@dp.message_handler(commands=['info'])
async def get_user_info(message: types.Message):
    # Get the user_id from the message
    user_id = message.from_user.id
    # Get the user's information
    user_info = await message.chat.get_member(user_id)
    print(user_info)
    # Get the user's status
    # user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=user_id)
    # print(user_status)
    # Send a message with the user's information
    text = f"Name: {user_info['user']['first_name']} {user_info['user']['last_name']}\n"
    text += f"Username: {user_info['user']['username']}\n"
    # text += f"Status: {user_status}\n"
    await message.reply(text)

# Start the bot
if __name__ == '__main__':
    start_polling(dp)
