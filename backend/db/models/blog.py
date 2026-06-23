from datetime import datetime
from db.base_class import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Blog(Base):
    __tablename__ = "blog"
    id: Mapped[int] = mapped_column(primary_key= True, index=True)
    tittle: Mapped[str] = mapped_column(String(50))
    slug: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column(String(300))
    author_id: Mapped[int] = mapped_column(ForeignKey("user_dt.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    is_active: Mapped[bool] = mapped_column(default=False)
    author = relationship("User", back_populates="blogs")

    # id = Column(Integer, primary_key= True)
    # tittle = Column(String)
    # slug = Column(String)
    # content = Column(String)
    # author_id = Column(Integer, ForeignKey= "user.id")
    # created_at = Column(DateTime, default=datetime.now)
    # is_active = Column(Boolean, default=False)