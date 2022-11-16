from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types


bank_card = ReplyKeyboardMarkup(resize_keyboard=True)

cards = [
    'KEB Hana Bank',
    'KB Kookmin Bank',
    'Standard Chartered',
    'Standard Chartered Korea',
    'Shinhan Bank',
    'Woori Bank',
    'Nonghyup Bank(농협)',
    'SC che il',
    'Citibank Korea',
    'HSBC',
    'KAKAO BANK',
    'doiji bank',
    'BOA',
    'JP MOGAN',
    'Chungug kungsan',
    'BNP',
    'Kei bank',
    'MG BANK(SEMAILKIMKO)',
    'CHUNGUG',
    'TOSIBANK',
    'KOKSE',
    'DGB Financial Group(Daegu Bank)',
    'BNK Financial Group',
    'Busan Bank',
    'Kyongnam Bank',
    'JB Financial Group',
    'Kwangju Bank',
    'Jeonbuk Bank',
    'Shinhan Financial Group',
    'Jeju Bank',
     "🔙 Ortga",
]

for x in cards:
  bank_card.add(KeyboardButton(x))






