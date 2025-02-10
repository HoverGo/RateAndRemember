from src.services.base_service import BaseService


class UserService(BaseService):

    async def create(self, instance_data):
        user = await self.super().create(instance_data)
        return user
    
    async def get_one(self, id: int):
        user = await self.super().get_one(id=id)
        return user
