from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db

category_cb = CallbackData('category', 'id', 'action')


def categories_markup():

    global category_cb
    
    markup = InlineKeyboardMarkup()
    for idx, title in db.fetchall('SELECT * FROM categories'):
        markup.add(InlineKeyboardButton(title, callback_data=category_cb.new(id=idx, action='view')))
    markup.add(InlineKeyboardButton("🛒 Корзина",callback_data= '\menu'))
    markup.add(InlineKeyboardButton("назад",callback_data= '\menu'))
    return markup