from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from setuptools import Command
from keyboards.default.markups import back_markup
from loader import db,dp
from handlers.user.catalog import process_catalog
product_cb = CallbackData('product', 'id', 'action')


def product_markup(idx='', price=0):

    global product_cb

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(f'Добавить в корзину - {price}₽', callback_data=product_cb.new(id=idx, action='add')))
    markup.add(InlineKeyboardButton('<< Назад', callback_data="Catalog"))
    return markup