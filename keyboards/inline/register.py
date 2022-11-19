from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



registration = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Registrasiya",callback_data="registrasiya"),
    ],
])