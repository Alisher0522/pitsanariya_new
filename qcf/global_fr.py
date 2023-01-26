from aiogram.types import Message


def ozgarmas_buyruqlarni_saralash(message: Message):
    print(message.text)
    data = message.text.replace(' ', '_')
    print(data)
    if data.startswith('/'):
        return data.lower()
    return data