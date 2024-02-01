from dataclasses import dataclass

from environs import Env


__all__ = ['Config', 'load_config']


@dataclass
class TgBot:
    token: str


@dataclass
class PostgresConfig:
    driver: str
    user: str
    password: str
    host: str
    port: int
    database: str


@dataclass
class RedisConfig:
    host: str
    port: int


@dataclass
class Config:
    tg_bot: TgBot
    postgres: PostgresConfig
    redis: RedisConfig


def load_config() -> Config:
    """
    Create the bot config class.
    """

    env: Env = Env()
    env.read_env()

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')),
                  postgres=PostgresConfig(driver=env('POSTGRES_DRIVER'),
                                          user=env('POSTGRES_USER'),
                                          password=env('POSTGRES_PASSWORD'),
                                          host=env('POSTGRES_HOST'),
                                          port=int(env('POSTGRES_PORT')),
                                          database=env('POSTGRES_DB')),
                  redis=RedisConfig(host=env('REDIS_HOST'),
                                    port=int(env('REDIS_PORT'))))
