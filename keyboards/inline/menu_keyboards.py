import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import db

# Turli tugmalar uchun CallbackData-obyektlarni yaratib olamiz
menu_cd = CallbackData("show_menu", "level", "employer_id", "company")
apply_company = CallbackData("employer", "company")


# Quyidagi funksiya yordamida menyudagi har bir element uchun calbback data yaratib olinadi
# Agar mahsulot kategoriyasi, ost-kategoriyasi va id raqami berilmagan bo'lsa 0 ga teng bo'ladi
def make_callback_data(level, employer_id="None",  company="0"):
    return menu_cd.new(
        level=level, employer_id=employer_id, company=company
    )

def apply_callback(employer,company):
    return apply_company.new(
         employer=employer, company=company
    )



# Bizning menu 3 qavat (LEVEL) dan iborat
# 0 - Ish beruvchilar
# 1 - Ish beruvchilar kompaniyasi
# 2 - Yagona kompaniya



# Kategoriyalar uchun keyboardyasab olamiz
async def employers_keyboard():
    # Eng yuqori 0-qavat ekanini ko'rsatamiz
    CURRENT_LEVEL = 0

    # Keyboard yaratamiz
    markup = InlineKeyboardMarkup(row_width=1)

    # Bazadagi barcha kategoriyalarni olamiz
    employers = await db.get_employers()
    
    # Har bir kategoriya uchun quyidagilarni bajaramiz:
    for employer in employers:
        # Kategoriyaga tegishli mahsulotlar sonini topamiz
        
        number_of_companies = await db.count_companies_by_employer(employer_id=employer['id'])
        employer_name = await db.select_user(id=employer['user_id_id'])
        try:
            employer_name = employer_name['username']
        except:
             employer_name = employer_name['full_name']
        # Tugma matnini yasab olamiz
        button_text = f"{employer_name} ({number_of_companies} dona)"

        # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1, employer_id=employer["id"]
        )

        # Tugmani keyboardga qo'shamiz
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Keyboardni qaytaramiz
    return markup


# Berilgan kategoriya ostidagi kategoriyalarni qaytaruvchi keyboard
async def companies_by_employer_keyboard(employer_user_id):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1)

    # Employerni ostidagi companiyalarni bazadan olamiz
    companies = await db.get_companies_by_employer(employer_id=employer_user_id)
    for company in companies:
        # # Kompaniyada nechta bosh o'rin  borligini tekshiramiz
        # number_of_free_places = await db.count_free_places(
        #     category_code=category, subcategory_code=subcategory["subcategory_code"]
        # )

        # Tugma matnini yasaymiz
        button_text = f"{company['companyname']}"

        # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1,
            employer_id=company['employer_name_id'],
            company=company["companyname"],
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Ortga qaytish tugmasini yasaymiz (yuqori qavatga qaytamiz)
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup



  

# Ostkategoriyaga tegishli mahsulotlar uchun keyboard yasaymiz
# async def items_keyboard(category, subcategory):
#     CURRENT_LEVEL = 2

#     markup = InlineKeyboardMarkup(row_width=1)

#     # Ost-kategorioyaga tegishli barcha mahsulotlarni olamiz
#     items = await db.get_products(category, subcategory)
#     for item in items:
#         # Tugma matnini yasaymiz
#         button_text = f"{item['productname']} - ${item['price']}"

#         # Tugma bosganda qaytuvchi callbackni yasaymiz: Keyingi bosqich +1 va kategoriyalar
#         callback_data = make_callback_data(
#             level=CURRENT_LEVEL + 1,
#             category=category,
#             subcategory=subcategory,
#             item_id=item["id"],
#         )
#         markup.insert(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )

#     # Ortga qaytish tugmasi
#     markup.row(
#         InlineKeyboardButton(
#             text="⬅️Ortga",
#             callback_data=make_callback_data(
#                 level=CURRENT_LEVEL - 1, category=category
#             ),
#         )
#     )
#     return markup


# Berilgan mahsulot uchun Xarid qilish va Ortga yozuvlarini chiqaruvchi tugma keyboard
# def item_keyboard(category, subcategory, item_id):
#     CURRENT_LEVEL = 3
#     markup = InlineKeyboardMarkup(row_width=1)
#     markup.row(
#         InlineKeyboardButton(
#             text=f"🛒 Xarid qilish", callback_data=buy_item.new(item_id=item_id)
#         )
#     )
#     markup.row(
#         InlineKeyboardButton(
#             text="⬅️Ortga",
#             callback_data=make_callback_data(
#                 level=CURRENT_LEVEL - 1, category=category, subcategory=subcategory
#             ),
#         )
#     )
#     return markup