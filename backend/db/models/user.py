from db.base_class import Base
from sqlalchemy import Integer, String, Boolean, DateTime, Column
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import List

class User(Base):
    __tablename__ = "user_dt"
    id: Mapped[int] = mapped_column(primary_key= True)
    email_id: Mapped[str] = mapped_column(unique= True)
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    blogs = relationship("Blog" ,back_populates="author")


    # id = Column(Integer, primary_key= True)
    # email_id = Column(String, unique= True)
    # password = Column(String, nullable=False)
    # is_activae = Column(Boolean, default=True)
    # blogs = relationship("Blog", back_populates="author")