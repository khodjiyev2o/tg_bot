from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun REGISTER statedan foydalanamiz

class REGISTER(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    name = State() # ism
    phoneNum = State() # Tel raqami
    cardNum = State()
    bank_name = State()