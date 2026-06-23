# Understand this 🙏
from typing import Any
# from sqlalchemy.orm import as_declarative, declared_attr, declarative_base
from sqlalchemy.orm import DeclarativeBase

# @as_declarative()
# class Base():
#     id: Any
#     __name__: str
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()

class Base(DeclarativeBase):
    pass



