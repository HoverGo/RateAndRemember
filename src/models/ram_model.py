from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, BigInteger
from base_model import BaseModel
from typing import Optional


class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str]
    full_name: Mapped[str]

    products: Mapped[list['Products']] = relationship("Products", back_populates='user')


class Categories(BaseModel):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)

    products: Mapped[list['Products']] = relationship("Products", back_populates='category')


class Products(BaseModel):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    name: Mapped[str]
    description: Mapped[Optional[str]]
    rate: Mapped[float]
    img_id: Mapped[Optional[str]]


    user: Mapped['User'] = relationship('User', back_populates='products')
    category: Mapped["Categories"] = relationship('Categories', back_populates='products')