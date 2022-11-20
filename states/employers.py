from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun Employers statedan foydalanamiz

class Employer(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    company = State() # ism
    submit = State()   