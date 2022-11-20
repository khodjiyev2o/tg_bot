from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



yes_no = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="XA",callback_data="xa"),
    ],
    [
        InlineKeyboardButton(text="YO'Q",callback_data="yoq"),
    ],
])


