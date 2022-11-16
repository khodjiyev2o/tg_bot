from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registration = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📝Registrasiya'),
            
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