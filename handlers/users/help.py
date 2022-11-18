from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from filters.private_chat import IsPrivate

@dp.message_handler(IsPrivate(),text_contains="Biz bilan bog'lanish")
async def bot_help(message: types.Message):
    text = ("Savollaringiz bo'lsa @khodjiyev2o ga murojat qilishingiz mumkin!")
    
    await message.answer(text)


@dp.message_handler(IsPrivate(),text_contains="Biz  haqimizda")
async def bot_help(message: types.Message):
    text = (
                "Founders : 👨🏻‍💻@khodjiyev2o",
                "© 2022-2023, All copyrights are reserved",
    )
    
    await message.answer("\n".join(text))



@dp.message_handler(IsPrivate(),text_contains="Qollanma")
async def bot_help(message: types.Message):
    text = (
                "- Ustida ishlanmoqda",
                "- Under the construction",
                "- В стадии строительства",
                "- 공사중",
                
    )
    
    await message.answer("\n".join(text))