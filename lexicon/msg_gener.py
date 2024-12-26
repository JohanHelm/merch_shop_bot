from lexicon.msg_texts import hello_msg, purchase_instruction, pay_instruction
from config_data.config import Seller


def create_hello_msg(seller: Seller):
    return f"{hello_msg}{purchase_instruction}{seller.seller_link}\n\n{pay_instruction} {seller.seller_num}"
