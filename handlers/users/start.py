from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    username  = message.from_user.full_name
    text = (f"Salom, {username}!",
            "Tekpe botga xush kelibsiz!")

    await message.answer("\n".join(text))