from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.register_start import registration
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    username  = message.from_user.full_name
    text = (f"Salom, {username}!",
            "Tekpe botga xush kelibsiz!",
            "Bot ni ishga tushirish uchun registrasiyadan utishingiz kerak!")

    await message.answer("\n".join(text),reply_markup=registration)
    