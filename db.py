from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Integer, Column, String
engine = create_engine('sqlite:///ecommerce.db', acho=True) # это типа создали Движок

SessionLocal = sessionmaker(bind=engine)   # сессии связи с базой со ссылкой на Движок
class Base(DeclarativeBase): #Образец базы "стандартной". Прокладка между классами, описывающими таблицы и DeclarativeBase
    pass



# class User(Base):          # такая констукция с нижепрописаным кодом позволяет не обращаться к SQL запросам
#     __tablename__ = 'user'    # по сути это класс таблицы. Имя таблицы 'user'
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)



