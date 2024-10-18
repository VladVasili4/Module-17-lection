from app.backend.db import Base
from sqlalchemy import Integer, Column, String, Boolean, ForeignKey # ForeignKey - ключ для связывания таблиц
from sqlalchemy import relationship
from app.models import *


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    product = relationship('Product', back_populates='category')  #!!! 'category' а не 'categories'


from sqlalchemy.schema import CreateTable
print(CreateTable(Category.__table__))