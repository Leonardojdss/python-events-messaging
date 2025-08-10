from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Costumer(Base):
    __tablename__ = 'costumers'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name_costumer = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    phone = Column(String(256), nullable=False)