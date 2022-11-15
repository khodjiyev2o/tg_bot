from aiogram import types
from aiogram.dispatcher import FSMContext,filters
from loader import dp
from states.register import REGISTER

PHONE_NUM = r'^[0-9]{3}-([0-9]{3}|[0-9]{4})-[0-9]{4}$'
#KOREAN_CARD = r'^9[0-9]{15}$'


@dp.message_handler(commands="registrasiya", state=None)
async def enter_test(message: types.Message):
    await message.answer("Ismingizni kiriting")
    await REGISTER.name.set()


@dp.message_handler(state=REGISTER.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("Isminigiz  muvaffaqiyatli  saqlandi!")
    text = (f"{name}!",
            "endi, telefon raqamingizni kiriting!",
            "Misol uchun: 010-9552-4141")
    await message.answer("\n".join(text))
    ##  moving to another state
    await REGISTER.phoneNum.set()


    
    

@dp.message_handler(filters.Regexp(PHONE_NUM),state=REGISTER.phoneNum)
async def regexp_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    phoneNum = message.text
    await state.update_data(
        {"phoneNum": phoneNum}
    )
    await message.answer("Telefon raqamingiz muvaffaqiyatli  saqlandi!")
   
    ##  moving to another state 

    text = (f"{name}",
            "endi iltimos, Koreya plastik karta raqamingizni kiriting!",
            "Misol uchun: 123456789101112")
    await message.answer("\n".join(text))
    await REGISTER.cardNum.set()



@dp.message_handler(state=REGISTER.cardNum)
async def state_example(message: types.Message, state: FSMContext):
    cardNum = message.text
    await state.update_data(
        {"cardNum": cardNum}
    )

    data = await state.get_data()
    name = data.get("name")
    await message.answer("Karta raqamingiz muvaffaqiyatli  saqlandi!")
    await message.answer(f"{name}, royhatdan muvaffaqiyatli o'tkaniz bilan tabriklaymiz!")



    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    cardNum = data.get("cardNum")
    phoneNum = data.get("phoneNum")

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Karta raqamingiz - {cardNum}\n"
    msg += f"Telefon: - {phoneNum}"
    await message.answer(msg)
    await state.finish()
    








