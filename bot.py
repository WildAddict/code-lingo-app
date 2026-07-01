from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

TOKEN = "ТВОЙ_ТОКЕН_БОТА"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):

    web_app_info = WebAppInfo(url="https://wildaddict.github.io/code-lingo-app/index.html")
    button = InlineKeyboardButton(text="Открыть CodeLingo", web_app=web_app_info)
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    
    await message.answer("Привет! Готов учить немецкие термины?", reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())