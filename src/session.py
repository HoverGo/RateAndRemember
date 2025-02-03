from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.config.local_settings import settings
from src.models.base_model import BaseModel
from collections.abc import AsyncGenerator


class DBSession():
    engine = create_async_engine(settings.get_db_url())
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async def get_db_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session() as session:
            yield session

    async def init_models(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.drop_all)
            await conn.run_sync(BaseModel.metadata.create_all)


session = DBSession()