
from aiogram.utils import executor
from create_bot import dp
import string
from handlers import client, admin, other



# a = 'sd@asf!d'
# print(a.translate(str.maketrans('', '', string.punctuation)))

async def on_startup(_):
    print("Bot online ga yuklandi")


client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
