from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


common_router = Router()


@common_router.message(Command("start"))
async def start(msg: Message):
    await msg.answer("""Мы можем беседовать часами, но на самом деле я только дожидаюсь, когда ты напишешь 'хорошо, что мы закончили'""")
    