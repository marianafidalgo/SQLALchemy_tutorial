from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    course = Column(String)
    age = Column(Integer)

    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship("Team", backref="team")

    #contact = relationship("Contact", uselist =False, back_populates="person")

    def __init__(self, name, course, age, team):
        self.name = name
        self.course = course
        self.age = age
        self.team = team