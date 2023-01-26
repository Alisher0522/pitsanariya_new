from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from qcf.global_fr import ozgarmas_buyruqlarni_saralash
from qcf.global_or import *



from create_bot import dp, bot

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

class FSMAdminChanel(StatesGroup):
    text = State


# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_comand(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Adminlik tastiqlandi:")
    await message.delete()


# @dp.message_handler(state=None, commands="Yuklash")
async def cm_start(message: types.Message):

    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply("Rasimni yuklang:")


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Nomini kiriting:")


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Tavshifini kiriting:")


# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("Narxini kiriting:")


# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        async with state.proxy() as data:
            await message.reply(str(data))
        await state.finish()


# @dp.message_handler(commands=['otmena'], state="*")
# @dp.message_handler(Text(equals='otmena', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state=FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if not current_state:
            return
        await state.finish()
        await message.reply('Ok')



def register_handler_admin(dpr: Dispatcher):
    dpr.register_message_handler(cancel_handler, lambda m: ozgarmas_buyruqlarni_saralash(m) in BUYRUQLAR['otmena'], state="*")
    dpr.register_message_handler(cancel_handler, Text(equals='otmena', ignore_case=True), state="*")
    dpr.register_message_handler(cm_start, commands=['Yuklash'], state=None)
    dpr.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dpr.register_message_handler(load_name, state=FSMAdmin.name)
    dpr.register_message_handler(load_description, state=FSMAdmin.description)
    dpr.register_message_handler(load_price, state=FSMAdmin.price)
    dpr.register_message_handler(make_changes_comand, commands=['moderator'], is_chat_admin=True)
