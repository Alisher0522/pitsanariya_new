
from aiogram.utils import executor
from create_bot import dp
import string


# a = 'sd@asf!d'
# print(a.translate(str.maketrans('', '', string.punctuation)))

async def on_startup(_):
    print("Bot online ga yuklandi")


from handlers import client, admin, other

client.register_handler_client(dp)
other.register_handler_other(dp)





executor.start_polling(dp, skip_updates=True, on_startup=on_startup)