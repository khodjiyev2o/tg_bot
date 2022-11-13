
import logging
from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")



#Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu Aleykum, tekpe botga xush kelibsiz!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu Aleykum, savollariz bolsa @khodjiyev2o ga muroojat qilishingiz mumkin!")



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)