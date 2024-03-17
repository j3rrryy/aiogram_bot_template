from aiogram import Bot, Router, F
from aiogram.types import Message, ReplyKeyboardRemove, \
    CallbackQuery, FSInputFile
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from lexicon import LEXICON_RU, LEXICON_EN, LEXICON_BOTH, \
    ERROR_LEXICON_RU, ERROR_LEXICON_EN, ERROR_LEXICON_BOTH
from .admin_handlers import admin_router
from middlewares import *


user_router: Router = Router()
user_router.include_router(admin_router)
user_router.message.middleware.register(AuthMiddleware())
user_router.callback_query.middleware.register(AuthMiddleware())
user_router.message.middleware.register(AntiFloodMiddleware())
user_router.callback_query.middleware.register(AntiFloodMiddleware())
