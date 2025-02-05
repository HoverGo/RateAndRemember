from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.base_repository import BaseRepository
from src.models.base_model import BaseModel
from src.schemas.base_schema import BaseSchema


class BaseService():

    def __init__(self, session: AsyncSession, repository: BaseRepository, model: BaseModel) -> None:
        self.repository = repository

    async def create(self, instance_data) -> BaseModel:
        instance = await self.repository.create(instance_data=instance_data)
        return instance
    
    async def get_one(self, **filters) -> BaseModel:
        instance = await self.repository.get_one(**filters)
        return instance

    async def get_all(self, **filters) -> list[BaseModel]:
        instance = await self.repository.get_all(**filters)
        return instance