from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()



class User(Base):
    __tablename__ = "user_account"

    id: Column = Column(Integer, primary_key=True)
    name: Column = Column(String(30))
    fullname: Column = Column(String(255))  # Spécifiez la longueur, par exemple 255

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

engine = create_engine(os.environ.get('DATABASE_URL'))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()