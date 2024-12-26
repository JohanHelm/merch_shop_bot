from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config_data.config import Seller
from lexicon.msg_gener import create_hello_msg


common_router = Router()


@common_router.message(Command("start"))
async def start(msg: Message, seller: Seller):
    if msg.from_user.id == seller.seller_tg_id:
        pass
    else:
        await msg.answer(text=create_hello_msg(seller))
