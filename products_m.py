from app.backend.db import Base
from sqlalchemy import Integer, Column, String, Boolean, ForeignKey, Float # ForeignKey - ключ для связывания таблиц
from sqlalchemy import relationship

class Product(Base):  # Собрали таблицу. Есть специальный способ, но мы решили сделать это так. Что за способ? не сказал.
    __tablename__ = 'products'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)     #   По хорошему, д.б. float, но лектор решил так
    image_url = Column(String)
    stock = Column(Integer)
    rating = Column(Float)
    is_active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey='categories.id') # Обеспечивает связь один ко многим?

    category = relationship('Category', back_populates='products')