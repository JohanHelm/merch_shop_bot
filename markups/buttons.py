from aiogram.types import InlineKeyboardButton


t_shirts_button = InlineKeyboardButton(
    text="Футболки",
    callback_data="assortment_t_shirts"
)

stickers_button = InlineKeyboardButton(
    text="Наклейки",
    callback_data="assortment_stickers"
)

chevrons_button = InlineKeyboardButton(
    text="Шевроны",
    callback_data="assortment_chevrons"
)


