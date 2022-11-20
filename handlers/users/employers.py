from typing import  Union
from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove,CallbackQuery
from aiogram.dispatcher import FSMContext,filters
from loader import dp,bot
from keyboards.inline import companies, yes_no
from filters.private_chat import IsPrivate
from keyboards.inline.menu_keyboards import (
    menu_cd,
    employers_keyboard,
    companies_by_employer_keyboard,
  
)

from states.employers import Employer

    

@dp.message_handler(text_contains="Ish beruvchi")
async def show_menu(message: types.Message):
    # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
    await list_employers(message)



# Employers qaytaruvchi funksiya. Callback query yoki Message qabul qilishi ham mumkin.

async def list_employers(message: Union[CallbackQuery, Message], **kwargs):
    # Keyboardni chaqiramiz
    markup = await employers_keyboard()

    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz
    if isinstance(message, Message):
        await message.answer("Ish beruvchini tanlang", reply_markup=markup)

    # Agar foydalanuvchidan Callback kelsa Callback matnini o'zgartiramiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)



async def list_companies_by_employer(callback:CallbackQuery, employer_id, **kwargs):
    # Keyboardni chaqiramiz
    markup = await companies_by_employer_keyboard(employer_id)
    
    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz

    await callback.message.edit_text(text="Kompaniyani tanlang", reply_markup=markup)
    

# @dp.message_handler(IsPrivate(),text_contains="Ortga", state=REGISTER)
# async def enter_name(message: types.Message,state:FSMContext):


    




# Yuqoridagi barcha funksiyalar uchun yagona handler
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # Foydalanuvchi so'ragan Employer
    employer_id = callback_data.get("employer_id")

    # Ost-kategoriya (har doim ham bo'lavermaydi)
    company = callback_data.get("company")

    

    # Har bir Level (qavatga) mos funksiyalarni yozib chiqamiz
    levels = {
        "0": list_employers,  # Kategoriyalarni qaytaramiz
        "1": list_companies_by_employer,  # Ost-kategoriyalarni qaytaramiz
         # Mahsulotlarni qaytaramiz
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, employer_id=employer_id, company=company
    )


@dp.callback_query_handler()
async def reconsider_decision(callback:CallbackQuery,state:FSMContext):
    await callback.message.edit_text(text="Haqiqatdanham yozdirilmoqchimisz?", reply_markup=yes_no.yes_no)
    await Employer.company.state()



@dp.callback_query_handler(text="xa")
async def reconsider_decision(callback:CallbackQuery,state:FSMContext):
    await callback.message.edit_text(text="Siz yozdirildiz!", reply_markup=yes_no.yes_no)
    await Employer.company.state()    