from src.schemas.base_schema import BaseSchema


class CreateUserSchema(BaseSchema):
    id: int
    username: str
    full_name: str

class CategoriesSchema(BaseSchema):
    id: int
    name: str

class CreateProductsSchema(BaseSchema):
    user_id: int
    category_id: int
    name: str
    description: str
    rate: float
    img_id: int

class ProductsSchema(CreateProductsSchema):
    id: int
