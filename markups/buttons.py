from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


# Создаем объекты инлайн-кнопок
t_shirts_button = InlineKeyboardButton(
    text="Футболки",
    callback_data="t_shirts_"
)
url_button_2 = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api'
)


