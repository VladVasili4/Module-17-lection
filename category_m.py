from app.backend.db import Base
from sqlalchemy import Integer, Column, String, Boolean, ForeignKey # ForeignKey - ключ для связывания таблиц
from sqlalchemy import relationship


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)