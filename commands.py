from aiogram import F, Router
from aiogram.types import Message, URLInputFile, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup
from aiogram.methods.send_message import SendMessage
import keyboard
import texts
from config import bot



router=Router()
page=0
check = 0

file_ids = ['AgACAgIAAxkBAAOGZnF0N7hpffNyYst0byIf68OJmgADed0xGxDGiUue8ySe9HtYWAEAAwIAA3kAAzUE',
            'AgACAgIAAxkBAAORZnF2NEg3qFov5x4c0rphrXhy0iQAAovdMRsQxolLMBkn6SyVZWEBAAMCAAN5AAM1BA',
            'AgACAgIAAxkBAAOIZnF0QBGritSlfSJ00zmU-TEhyQkAAnvdMRsQxolLM12xfnO2PEsBAAMCAAN4AAM1BA'
            ]



@router.message(CommandStart()) #декоратор message
async def cmd_start(message: Message):   # ассинх функция. При команде старт отправляет сообщение
    await message.answer(f'Привет, <b>{message.from_user.first_name}</b>! ',reply_markup= keyboard.main_keyboard)  #


@router.message(F.text.lower()=='каталог')
async def upload_photo(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAOGZnF0N7hpffNyYst0byIf68OJmgADed0xGxDGiUue8ySe9HtYWAEAAwIAA3kAAzUE',
                               caption='Арт в полный рост. Стоимость - 1200р. За подробностями в личные сообщения.',
                               reply_markup=keyboard.catalog)

@router.message(F.text.lower()=='faq')
async def faq(message: Message):
    await message.answer(text=texts.faq)


@router.message(F.text.lower()=='донат')
async def donat(message:Message):
    await message.answer(text='Данная функция пока недоступна. Ждите обновлений.')
    

@router.callback_query(F.data.startswith('btn_increase'))
async def catalog_handler(callback: CallbackQuery):
    global page
    if page==2:
        page=-1
    page+=1
    await callback.message.answer_photo(file_ids[page],caption= texts.txts[page],reply_markup=keyboard.catalog)


@router.callback_query(F.data.startswith('btn_decrease'))
async def catalog_handler(callback: CallbackQuery):
    global page
    if page==-3:
        page=0
    page-=1
    await callback.message.answer_photo(file_ids[page],caption=texts.txts[page],reply_markup=keyboard.catalog)
    print(page)



@router.callback_query(F.data.startswith('order'))
async def order_p1(callback: CallbackQuery):
    global check
    await callback.message.answer(text='Что конкретно нужно нарисовать?')
    check+=1


@router.message(F.text)
async def ordering(message:Message):
    global check
    global aidi
    aidi = message.from_user.id
    if check==1:
        await bot.send_message(chat_id='503352199',text=message.text,reply_markup=keyboard.order_check)
        check=0



@router.callback_query(F.data.startswith('yes'))
async def accept(callback:CallbackQuery):
    await callback.message.answer(text='Заказ принят')
    await callback.bot.send_message(chat_id = aidi, text = f'Твой заказ получен. Держи ник художника: @Pancake_boy1987')



@router.callback_query(F.data.startswith('no'))
async def decline(callback:CallbackQuery):
    await callback.bot.send_message(chat_id=aidi, text = 'К сожелнию, художник не собирается такое рисовать. Придумай что-то получше.')


@router.message(F.photo)
async def upload_photo2(message:Message):
    photo_data = message.photo[-1]
    await message.answer(f'{photo_data}')



@router.message(F.text.lower()=='в меню')
async def back(message:Message):
    await message.answer('Меню',reply_markup=keyboard.main_keyboard)