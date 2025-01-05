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

admin_router: Router = Router()
