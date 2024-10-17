from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Integer, Column, String
engine = create_engine('sqlite:///ecommerce.db', acho=True)

SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass



# class User(Base):          # такая констукция с нижепрописаным кодом позволяет не обращаться к SQL
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)



