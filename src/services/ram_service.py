from services.base_service import BaseService


class UserService(BaseService):

    async def create(self, id, username, full_name):
        user = await super().create(id=id, username=username, full_name=full_name)
        return user
    
    async def get_one(self, id: int):
        user = await super().get_one(id=id)
        return user
