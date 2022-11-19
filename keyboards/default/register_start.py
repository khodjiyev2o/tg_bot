from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registration = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='👨‍💼Ish beruvchi'),
            
        ],
        [
            KeyboardButton(text='📄Qollanma'),
        ],
        [
            KeyboardButton(text="📞Biz bilan bog'lanish"),
        ],
        [
            KeyboardButton(text='⚙️Biz  haqimizda'),
        ],
    ],
    resize_keyboard=True
)