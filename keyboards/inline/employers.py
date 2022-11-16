from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



employers = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Jorabek Djurayev",callback_data="jurabek"),
    ],
    [
        InlineKeyboardButton(text="Saliyevich Salohiddin",callback_data="salohiddin"),
    ],
])