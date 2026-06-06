import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Твой проверенный токен!
TOKEN = "8984772458:AAFdF0nuzYCoT9gSw8Oe6JabfAHyOKVDD7k"

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

# Срабатывает на /start
@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 🐧\n"
        "Я твой продвинутый помощник по Linux. Выбери нужный раздел на кнопках ниже:",
        reply_markup=main_keyboard
    )

# Кнопка "Шпаргалка"
@dp.message(F.text == "📚 Шпаргалка по командам")
async def show_cheatsheet(message: Message):
    text = (
        "**🔥 Главные команды для терминала:**\n\n"
        "**Обновление системы:**\n"
        "• Arch/CachyOS: `sudo pacman -Syu`\n"
        "• Ubuntu/Debian: `sudo apt update && sudo apt upgrade`\n\n"
        "**Управление файлами:**\n"
        "• `ls` — посмотреть файлы в папке\n"
        "• `cd имя_папки` — перейти в папку\n"
        "• `mkdir имя` — создать новую папку"
    )
    await message.answer(text, parse_mode="Markdown")

# Кнопка "Кастомизация"
@dp.message(F.text == "⚙️ Кастомизация и Темы")
async def show_customization(message: Message):
    text = (
        "**🎨 Как сделать Linux красивым:**\n\n"
        "1. Ищи крутые конфиги на GitHub по запросу **dotfiles**.\n"
        "2. Загляни на Reddit в сообщество **r/unixporn** — там люди со всего мира делятся своими рабочими столами.\n"
        "3. Для автоматизации кликов и макросов используй утилиты вроде `xmacro` или скрипты автоматизации."
    )
    await message.answer(text, parse_mode="Markdown")

# НОВАЯ КНОПКА: Решение проблем
@dp.message(F.text == "🛠️ Что делать, если... (Решение проблем)")
async def show_troubleshooting(message: Message):
    text = (
        "**⚠️ Скорая помощь при проблемах в Linux:**\n\n"
        "**1. Зависла программа и не закрывается:**\n"
        "• Нажми `Ctrl + Alt + T` (откроется терминал).\n"
        "• Введи команду `xkill` — появится курсор-крестик. Нажми им на зависшее окно, и оно тут же закроется!\n\n"
        "**2. Пропал интернет или сеть «глючит»:**\n"
        "• Перезапусти сетевую службу командой:\n"
        "`sudo systemctl restart NetworkManager`\n\n"
        "**3. Система пишет, что диск переполнен:**\n"
        "• Очисти кэш пакетов Arch/CachyOS:\n"
        "`sudo pacman -Scc` (удалит старые загруженные файлы пакетов)."
    )
    await message.answer(text, parse_mode="Markdown")

# Запуск бота
async def main():
    print("Бот успешно обновлен, запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
