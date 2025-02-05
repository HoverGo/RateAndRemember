from src.repositories.base_repository import BaseRepository
from src.models.ram_model import User

class UserRepository(BaseRepository):

    async def create(self, instance_data) -> User:
        instance = await self.super().create(instance_data)
        return instance
    
    async def get_one(self, id: int) -> User:
        user = self.super().get_one(id=id)
        return user


