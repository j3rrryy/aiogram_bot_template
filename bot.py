import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from config import load_config
from database import get_postgres_sessionmaker
from handlers import user_router
from keyboards import set_main_menu


logger = logging.getLogger(__name__)


async def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config = load_config()
    properties = DefaultBotProperties(parse_mode='HTML')

    storage: RedisStorage = RedisStorage(
        redis=Redis(host=config.redis.host,
                    port=config.redis.port))

    bot: Bot = Bot(token=config.tg_bot.token, default=properties)
    disp: Dispatcher = Dispatcher(storage=storage)

    await set_main_menu(bot)

    disp.include_router(user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await disp.start_polling(bot, sessionmaker=get_postgres_sessionmaker())


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error('Bot stopped!')
        print(e)
