from functools import wraps

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.config import load_config


def _get_sessionmaker() -> async_sessionmaker[AsyncSession]:
    config = load_config()
    postgres_url = URL.create(
        drivername=config.postgres.driver,
        username=config.postgres.user,
        password=config.postgres.password,
        host=config.postgres.host,
        port=config.postgres.port,
        database=config.postgres.database,
    )

    async_engine = create_async_engine(url=postgres_url, pool_pre_ping=True)
    session_maker = async_sessionmaker(bind=async_engine, class_=AsyncSession)
    return session_maker


_sessionmaker = _get_sessionmaker()


def get_session(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with _sessionmaker() as session:
            result = await func(*args, **kwargs, session=session)
            return result

    return wrapper
