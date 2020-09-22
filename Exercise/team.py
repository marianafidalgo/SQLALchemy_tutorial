from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from base import Base


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    proj_name = Column(String)
    money = Column(Integer)


    def __init__(self, name, proj_name, money):
        self.name = name
        self.proj_name = proj_name
        self.money = money