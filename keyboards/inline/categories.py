from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
""", CallbackQuery """
from aiogram.utils.callback_data import CallbackData
from loader import db
from handlers.user.menu import admin_menu
from loader import dp, db
category_cb = CallbackData('category', 'id', 'action')
def categories_markup():

    global category_cb
    
    markup = InlineKeyboardMarkup()
    for idx, title in db.fetchall('SELECT * FROM categories'):
        markup.add(InlineKeyboardButton(title, callback_data=category_cb.new(id=idx, action='view')))
    # markup.add(InlineKeyboardButton('<< Назад', callback_data=category_cb.new(id='-', action='list')))
    return markup


# @dp.callback_query_handler(category_cb.filter(action='list'))
# async def query_show_list(query: CallbackQuery):
#     await query.message.edit_text('menu', reply_markup=admin_menu())