from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove,CallbackQuery
from aiogram.dispatcher import FSMContext,filters
from loader import dp,bot
from states.register import REGISTER
from keyboards.default.bank_card import bank_card
from keyboards.default.next_back import back
from keyboards.default.register_start import registration
from keyboards.inline.register import registration as registr_inline
from filters.private_chat import IsPrivate


PHONE_NUM = r'^[0-9]{3}-([0-9]{3}|[0-9]{4})-[0-9]{4}$'

BANK_CARD = r"^[0-9]*$"



@dp.message_handler(IsPrivate(),text_contains="Ortga", state=REGISTER)
async def enter_name(message: types.Message,state:FSMContext):
  username  = message.from_user.full_name
  text = (f"Xush kelibsiz, {username}!",
            "📦Tekpe botga xush kelibsiz!",
            "🤖Bot ni ishga tushirish uchun registrasiyadan utishingiz kerak!")
  await state.finish()
  await message.answer("\n".join(text),reply_markup=registr_inline)



@dp.callback_query_handler(text="registrasiya")
async def enter_name(call: CallbackQuery,state:FSMContext):
    await bot.send_message(text="Ismingizni kiriting",reply_markup=back,chat_id=call.from_user.id)
    await REGISTER.name.set()


@dp.message_handler(IsPrivate(),state=REGISTER.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("Isminigiz  muvaffaqiyatli  saqlandi!")
    text = (f"{name}!", 
            "endi, 📞telefon raqamingizni kiriting!",
            "Misol uchun: 010-9552-4141")
    await message.answer("\n".join(text),reply_markup=back)
    ##  moving to another state
    await REGISTER.phoneNum.set()


@dp.message_handler(IsPrivate(),filters.Regexp(PHONE_NUM),state=REGISTER.phoneNum)
async def regexp_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    phoneNum = message.text
    await state.update_data(
        {"phoneNum": phoneNum}
    )
    await message.answer("Telefon raqamingiz muvaffaqiyatli  saqlandi!")
   
    ##  moving to another state 
    await REGISTER.bank_name.set()
    await message.answer("Endi, Bankni tanlang", reply_markup=bank_card)
    

@dp.message_handler(IsPrivate(),state=REGISTER.bank_name)
async def show_bank_names(message: Message,state: FSMContext):
    bank_name = message.text
    await state.update_data(
        {"bank_name":bank_name}
    )
    
     ##  moving to another state 
    data = await state.get_data()
    name = data.get("name")
    text = (f"{name},",
            "endi iltimos,💳 Koreya plastik karta raqamingizni  kiriting!",
            "Misol uchun: 123456789101112")
    await message.answer("\n".join(text),reply_markup=back)
    await REGISTER.cardNum.set()




@dp.message_handler(filters.Regexp(BANK_CARD),state=REGISTER.cardNum)
async def state_example(message: types.Message, state: FSMContext):
    cardNum = message.text
    await state.update_data(
        {"cardNum": cardNum}
    )

    data = await state.get_data()
    name = data.get("name")
    await message.answer("Karta raqamingiz muvaffaqiyatli  saqlandi!",reply_markup=ReplyKeyboardRemove())
    await message.answer(f"{name}, royhatdan muvaffaqiyatli o'tkaniz bilan tabriklaymiz!")



    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    cardNum = data.get("cardNum")
    phoneNum = data.get("phoneNum")
    bank_name = data.get("bank_name")


    msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Karta raqamingiz - {cardNum}\n"
    msg += f"Bank nomi - {bank_name}\n"
    msg += f"Telefon: - {phoneNum}"
    await message.answer(msg)
    await state.finish()
    








