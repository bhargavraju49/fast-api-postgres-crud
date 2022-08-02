from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from config.postgres import Base


class Person(Base):
    __tablename__ = "persons"

    personid = Column(Integer, primary_key=True, index=True)
    lastname = Column(String(255), index=True)
    firstname = Column(String(255), index=True)
    address = Column(String(255), index=True)
    city = Column(String(255), index=True)
