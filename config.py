from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

TOKEN ='7489927664:AAGZFagSdY_pQuZ7KOGsh76F2F-g4UO95QU'

#user_id = 503352199
bot = Bot(token=TOKEN, default=DefaultBotProperties(
    parse_mode=ParseMode.HTML))  # переменная бот,юзающая класс Бот default = DefaultBotProperties(parse_mode='HTML')
