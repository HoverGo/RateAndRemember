from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from models.base_model import BaseModel

class BaseRepository:

    def __init__(self, session: AsyncSession, model: BaseModel):
        self.session = session
        self.model = model

    async def create(self, **instance_data) -> BaseModel:
        async with self.session() as session:
            instance_new = self.model(**instance_data)
            session.add(instance_new)
            await session.flush()
            await session.commit()
            return instance_new
    
    async def get_one(self, **filters) -> BaseModel:
        async with self.session() as session:
            query = select(self.model).filter_by(**filters)
            result = await session.execute(query)
            instance = result.scalar_one_or_none()
            return instance
        
    async def get_all(
            self,
            order: str = 'id',
            limit: int = 10,
            offset: int = 0
            ) -> list[BaseModel]:
        async with self.session() as session:
            query = select(self.model).order_by(text(order)).offset(offset).limit(limit)
            result = await session.execute(query)
            instances = result.scalars().all()
            return instances
        


    
        