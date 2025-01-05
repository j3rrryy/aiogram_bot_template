from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, FSInputFile, Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.lexicon import (
    ERROR_LEXICON_BOTH,
    ERROR_LEXICON_EN,
    ERROR_LEXICON_RU,
    LEXICON_BOTH,
    LEXICON_EN,
    LEXICON_RU,
)
from src.middlewares import AntiFloodMiddleware, AuthMiddleware

from .admin_handlers import admin_router

user_router: Router = Router()
user_router.include_router(admin_router)
user_router.message.middleware.register(AuthMiddleware())
user_router.callback_query.middleware.register(AuthMiddleware())
user_router.message.middleware.register(AntiFloodMiddleware())
user_router.callback_query.middleware.register(AntiFloodMiddleware())
