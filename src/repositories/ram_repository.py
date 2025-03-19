from repositories.base_repository import BaseRepository
from models.ram_model import User

class UserRepository(BaseRepository):

    async def create(self, id, username, full_name) -> User:
        user = await super().create(id=id, username=username, full_name=full_name)
        return user
    
    async def get_one(self, id: int) -> User:
        user = await super().get_one(id=id)
        return user


