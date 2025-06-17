
# Telegram Bot: Транслитерация ФИО по Приказу МИД

Этот бот принимает ФИО на кириллице и возвращает его транслитерацию в латинице согласно Приказу МИД России от 12.02.2020 № 2113.

## Возможности

– Принимает текстовое сообщение от пользователя (ФИО)
– Возвращает транслитерацию по утверждённым правилам
– Логирует все обращения
– Развёрнут в Docker-контейнере

## Установка и запуск

1. Клонируй репозиторий:

git clone [https://github.com/твое\_имя\_пользователя/telegram-fio-bot.git](https://github.com/твое_имя_пользователя/telegram-fio-bot.git)
cd telegram-fio-bot

2. Создай и активируй виртуальное окружение (если нужно):

python3 -m venv venv
source venv/bin/activate (для Windows: venv\Scripts\activate)

3. Установи зависимости:

pip install -r requirements.txt

4. Добавь файл .env со своим токеном:

BOT\_TOKEN=твой\_токен\_бота

5. Запусти бота:

python bot.py

## Docker

1. Собери образ:

docker build -t fio-translit-bot .

2. Запусти контейнер:

docker run -d --env-file .env fio-translit-bot

## Структура проекта

.
├── bot.py — основной файл бота
├── translit.py — модуль с правилами транслитерации
├── requirements.txt — зависимости проекта
├── .env — переменные окружения (не добавляй в git!)
├── .gitignore
├── README.md
