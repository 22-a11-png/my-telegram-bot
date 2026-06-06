import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp import web

# Твой НОВЫЙ токен, который сбросил все конфликты
TOKEN = "8984772458:AAHEPJEf6wPWq7XSpdBR2RhSmSofDsBJkyk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаем меню с ТРЕМЯ кнопками
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Шпаргалка по командам")],
        [KeyboardButton(text="⚙️ Кастомизация и Темы")],
        [KeyboardButton(text="🛠️ Что делать, если... (Решение проблем)")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! Я твой бот, запущенный на бесплатном сервере Linux в облаке!",
        reply_markup=main_keyboard
    )

# Хак для Render: создаем микро-веб-сайт, который слушает нужный порт
async def handle(request):
    return web.Response(text="Бот запущен и работает!")

async def start_webserver():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"--- Веб-сервер для Render запущен на порту {port} ---")

# Главная функция запуска всего приложения
async def main():
    await start_webserver()
    print("--- Бот начинает опрос Telegram (Polling) ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
