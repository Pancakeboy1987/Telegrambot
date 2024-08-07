from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties



#user_id = 503352199
bot = Bot(token=TOKEN, default=DefaultBotProperties(
    parse_mode=ParseMode.HTML))  # переменная бот,юзающая класс Бот default = DefaultBotProperties(parse_mode='HTML')
