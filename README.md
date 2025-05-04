# 🤖 Friends Club Telegram Bot

Данный проект представляет собой Telegram-бота для управления клубом друзей. Бот предоставляет функциональность для взаимодействия с участниками клуба, включая регистрацию, управление мероприятиями и отправку уведомлений.

## 🚀 Начало работы

### 📦 Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/BuryatisLesa/Friends_Club_TelegramBot.git
   cd Friends_Club_TelegramBot
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Настройте переменные окружения или отредактируйте `config.py` с вашими настройками, включая токен бота и параметры базы данных.

5. Запустите бота:

   ```bash
   python run.py
   ```

## 🧩 Функциональность

- Регистрация новых участников клуба
- Управление списком мероприятий
- Отправка уведомлений участникам
- Интеграция с базой данных для хранения информации

## 🗂️ Структура проекта

```plaintext
Friends_Club_TelegramBot/
├── app/                 # Основное приложение бота
├── media/               # Медиа-файлы
├── venv/                # Виртуальное окружение
├── config.py            # Конфигурационный файл
├── friendsclub.sql      # SQL-скрипт для создания базы данных
├── run.py               # Точка входа для запуска бота
└── requirements.txt     # Список зависимостей
```

## 🛠️ Используемые технологии

- Python 3.x
- Telegram Bot API
- SQLite
- Библиотеки: `python-telegram-bot`, `sqlite3`

## 👤 Автор

**Константин Санданов**  
📧 [kostyansandanov@gmail.com](mailto:kostyansandanov@gmail.com)
