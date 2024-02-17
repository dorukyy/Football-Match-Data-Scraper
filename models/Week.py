from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from base import Base


class Week(Base):
    __tablename__ = 'weeks'

    id = Column(Integer, primary_key=True)
    start_date = Column(String)
    end_date = Column(String)

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
