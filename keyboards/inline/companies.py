from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



jurabek = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Okcheon CJ",callback_data="jurabek_okcheon"),
    ],
    [
        InlineKeyboardButton(text="Chongju CJ",callback_data="jurabek_chongju"),
    ],
])