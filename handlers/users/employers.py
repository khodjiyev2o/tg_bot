from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove,CallbackQuery
from aiogram.dispatcher import FSMContext,filters
from loader import dp,bot
from keyboards.inline import employers,companies
from filters.private_chat import IsPrivate


@dp.message_handler(IsPrivate(),text_contains="Ish beruvchi")
async def enter_name(message: Message):
    await message.answer("Ish beruvchini tanlang",reply_markup=employers.employers)
    



@dp.callback_query_handler(IsPrivate(),text="salohiddin")
async def enter_name(call: CallbackQuery):
    msg = "Salohiddin Saliyevichni tanladingiz!"
    await bot.send_message(chat_id=call.from_user.id, text=msg)
    await call.answer(cache_time=60)
  


@dp.callback_query_handler(IsPrivate(),text="jurabek")
async def enter_name(call: CallbackQuery):
    msg = "Jurabek Djurayevga tegishli 📦pochta kompaniyasini tanlang!"
    await bot.send_message(chat_id=call.from_user.id, text=msg,reply_markup=companies.jurabek)
    await call.answer(cache_time=60)



@dp.callback_query_handler(IsPrivate(),text="jurabek_okcheon")
async def enter_name(call: CallbackQuery):
    msg = "Okcheon CJ ga Jurabek Djurayevga  yozdilirdiz!✅"
    await bot.send_message(chat_id=call.from_user.id, text=msg)
    await call.answer(cache_time=60)


@dp.callback_query_handler(IsPrivate(),text="jurabek_chongju")
async def enter_name(call: CallbackQuery):
    msg = "Chongju  CJ ga Jurabek Djurayevga  yozdilirdiz!✅"
    await bot.send_message(chat_id=call.from_user.id, text=msg)
    await call.answer(cache_time=60)