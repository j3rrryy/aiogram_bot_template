from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject

from src.database import User, get_sessionmaker


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, (Message, CallbackQuery)):
            tg_user_id = event.from_user.id

            async with get_sessionmaker()() as session:
                async with session.begin():
                    user = await session.get(User, tg_user_id)
                    data["user"] = user
                    return await handler(event, data)
