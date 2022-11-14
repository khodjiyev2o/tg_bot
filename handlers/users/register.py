from aiogram import types
from aiogram.dispatcher import FSMContext,filters
from loader import dp


PHONE_NUM = r'^[0-9]{3}-([0-9]{3}|[0-9]{4})-[0-9]{4}$'
KOREAN_CARD = r'^9[0-9]{15}$'



@dp.message_handler(commands="registrasiya")
async def set_state(msg: types.Message, state: FSMContext):
    """Foydalanuvchi registrasiya state ichida"""
    username  = msg.from_user.full_name
    text = (f"{username}!",
            "Royhatdan utish uchun telefon raqamingizni kiriting!",
            "Misol uchun: 010-9552-4141")
    await msg.answer("\n".join(text))
    ##  moving to another state
    await state.set_state('phone_number')
    

@dp.message_handler(filters.Regexp(PHONE_NUM),state='phone_number')
async def regexp_phone(msg: types.Message, state: FSMContext):
    await msg.answer("Telefon raqamingiz muvaffaqiyatli  saqlandi!")
   
    ##  moving to another state 
    await state.set_state('card_number')
    text = (f"{msg.from_user.full_name}!",
            "endi iltimos, Koreya plastik karta raqamingizni kiriting!",
            "Misol uchun: 010-9552-4141")
    await msg.answer("\n".join(text))



@dp.message_handler(filters.Regexp(KOREAN_CARD),state='card_number')
async def state_example(msg: types.Message, state: FSMContext):
    await msg.answer("Karta raqamingiz muvaffaqiyatli  saqlandi!")
    await msg.answer(f"{msg.from_user.full_name}, royhatdan muvaffaqiyatli o'tkaniz bilan tabriklaymiz!")
    await state.finish()
    







