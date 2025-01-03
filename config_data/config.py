from dataclasses import dataclass
from environs import Env
from pathlib import Path

@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    # admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Seller:
    seller_link: str
    seller_num: int
    seller_tg_id: int



@dataclass
class Config:
    tg_bot: TgBot
    seller: Seller
    # db: DatabaseConfig


def load_config(path: Path | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"),
            # admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        seller=Seller(
            seller_link=env("SELLER_LINK"),
            seller_num=env("SELLER_NUM"),
            seller_tg_id=env("SELLER_TG_ID")
        ),
        # db=DatabaseConfig(
        #     database=env('DATABASE'),
        #     db_host=env('DB_HOST'),
        #     db_user=env('DB_USER'),
        #     db_password=env('DB_PASSWORD')
        # )
    )