from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.register_start import registration
from keyboards.inline.register import registration as registr_inline
from loader import dp, db, bot 
from filters.private_chat import IsPrivate
import asyncpg
from data.config import ADMINS

@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message): 
    username  = message.from_user.full_name
    try:

        user = await db.add_user(full_name=message.from_user.full_name,
                                 username=message.from_user.username,
                                 telegram_id=message.from_user.id)
        user = await db.select_user(telegram_id=message.from_user.id)
        count = await db.count_users()
        msg = f"{user[1]} has been succesfully added to the  database.\nThere are currently {count} users in the database ."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except asyncpg.exceptions.UniqueViolationError:
        count = await db.count_users()
        user = await db.select_user(telegram_id=message.from_user.id)
        msg = f"{user[1]} is already in  the database.\nThere are currently {count} users in the database ."
        await bot.send_message(chat_id=ADMINS[0], text=msg)


    text = (f"Salom, {username}!",
            "📦Tekpe botga xush kelibsiz!",
            "🤖Bot ni ishga tushirish uchun registrasiyadan utishingiz kerak!")

    await message.answer("\n".join(text),reply_markup=registr_inline)
    
    # ADMINGA xabar beramiz
    
    
@dp.message_handler(IsPrivate(),commands="allusers")
async def bot_start(message: types.Message): 
        count = await db.count_users()
        users = await db.select_all_users()
        i = 1
        text = f"There are : {count} users in the database.\n"
        for user in users:
                if user[2]:
                        text += f"{i}.@{user[2]}\n"
                else:
                        text += f"{i}.{user[1]}\n"
                i+=1
        await message.answer(text)
