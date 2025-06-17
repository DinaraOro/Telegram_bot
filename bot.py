# 1.Импорт библиотек
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message             # ловим все обновления этого типа 
# from aiogram.filters.command import Command   # обрабатываем команды /start, /help и другие
from aiogram.filters import Command
import sys


translit_table = {
    # строчные
    "а": "A",
    "б": "B",
    "в": "V",
    "г": "G",
    "д": "D",
    "е": "E",
    "ё": "E",
    "ж": "ZH",
    "з": "Z",
    "и": "I",
    "й": "I",
    "к": "K",
    "л": "L",
    "м": "M",
    "н": "N",
    "о": "O",
    "п": "P",
    "р": "R",
    "с": "S",
    "т": "T",
    "у": "U",
    "ф": "F",
    "х": "KH",
    "ц": "TS",
    "ч": "CH",
    "ш": "SH",
    "щ": "SHCH",
    "ы": "Y",
    "ъ": "IE",
    "э": "E",
    "ю": "IU",
    "я": "IA",
    " ": " ",
    # заглавные
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TS",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Ъ": "IE",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
}


# 2. Инициализация объектов
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)                        # Создаем объект бота
dp = Dispatcher()                             # Создаем объект диспетчера. Все хэндлеры(обработчики) должны быть подключены к диспетчеру


# Домашнее Задание
# - Включить запись log в файл
# - Бот принимает кириллицу отдаёт латиницу в соответствии с Приказом МИД по транслитерации
# - Бот работает из-под docker контейнера

logging.basicConfig(
    level=logging.INFO,
    format="[ %(levelname)s ] %(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log", mode='w', encoding='utf-8'),  # файл
        logging.StreamHandler(sys.stdout),  # Выводи логи не только в файл, но и в консоль, используя sys.stdout
    ]
)
# level=logging.INFO — минимальный уровень логов (INFO и выше).
# format="[ %(levelname)s ] %(asctime)s - %(message)s" — формат вывода логов (уровень, время, сообщение).
# handlers=[...] — куда писать логи:
# logging.FileHandler("bot.log", mode='w', encoding='utf-8') — в файл bot.log, перезаписывая его, с кодировкой UTF-8.
# logging.StreamHandler(sys.stdout) — в консоль (stdout), чтобы видеть логи при запуске, например в Docker.


# 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

# 4. Делаем транслитирацию
def transliterate(text: str) -> str:
    result = ""
    for char in text:
        result += translit_table.get(char, char.upper())
    return result
    
# 4. Обработка/Хэндлер на любые сообщения для транслетирации

@dp.message()
async def send_translit_fio(message: Message):
    text = message.text
    user_name = message.from_user.full_name
    user_id = message.from_user.id

    latin = transliterate(text)
    logging.info(f"{user_name} ({user_id}) отправил: {text} -> {latin}")
    await message.answer(latin)


# 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)
