from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Каталог'),
            KeyboardButton(text='Донат'),
            KeyboardButton(text='FAQ')

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню',
    selective= True

)



catalog = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text ='Вперёд', callback_data='btn_increase'),
         InlineKeyboardButton(text='Назад',callback_data='btn_decrease'),
         InlineKeyboardButton(text ='Заказать', callback_data= 'order')
     ],
    ],one_time_keyboard=True)

order_check = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text = 'Согласиться',callback_data='yes'),
         InlineKeyboardButton(text = 'Отказать',callback_data='no')
        ],
    ],one_time_keyboard=True
)