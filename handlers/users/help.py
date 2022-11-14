from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "Savollaringiz bo'lsa @khodjiyev2o ga murojat qilishingiz mumkin!")
    
    await message.answer("\n".join(text))
