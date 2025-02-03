from src.schemas.base_schema import BaseSchema


class UserSchema(BaseSchema):
    id: int
    username: str
    full_name: str

class CategoriesSchema(BaseSchema):
    name: str

class CreateProductsSchema(BaseSchema):
    user_id: int
    category_id: int
    name: str
    description: str
    rate: float
    img_id: int
