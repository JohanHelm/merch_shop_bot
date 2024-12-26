from aiogram.types import InlineKeyboardMarkup

from markups.buttons import *


catalog_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[t_shirts_button],
                     [stickers_button],
                     [chevrons_button]])