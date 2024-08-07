import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, CommandObject
from config import TOKEN
from handlers import commands
from aiogram.methods.send_message import SendMessage
from config import bot




async def main():
    global bot
    dp = Dispatcher()  # диспетчер, через который отслеживаются сообщения
    dp.include_routers(commands.router)
    await bot.delete_webhook(drop_pending_updates=True) #бот отвечает на комманду единожды, не зависимо от того,сколько раз его вызвали
    await  dp.start_polling(bot)






if __name__=='__main__':
    logging.basicConfig(level = logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT')

