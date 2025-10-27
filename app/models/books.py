from sqlalchemy import Column,String,Integer,Float
from app.db.database import Base

class Book(Base):
    __tablename__ = 'books'

    id     = Column(Integer,primary_key=True, unique=True,index=True)
    title  = Column(String(256),nullable=False)
    author = Column(String(100),nullable=False)
    genre  = Column(String(100),nullable=False)
    year   = Column(Integer,nullable=False)
    rating = Column(Float,nullable=False)



