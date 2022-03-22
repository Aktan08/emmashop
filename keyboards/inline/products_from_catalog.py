from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db
from .categories import category_cb
product_cb = CallbackData('product', 'id', 'action')


def product_markup(idx='', price=0):

    global product_cb

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(f'Добавить в корзину - {price}₽', callback_data=product_cb.new(id=idx, action='add')))
    markup.add(InlineKeyboardButton('<< Назад', callback_data=category_cb.new(id='-', action='list')))
    return markup