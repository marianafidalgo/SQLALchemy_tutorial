from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from base import Base


class Contact(Base):
    __tablename__ ='contacts'

    id = Column(Integer, primary_key=True)

    phone = Column(Integer)
    email = Column(String)

    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person",  backref=backref("contacts", uselist=False))

    auth = Column(Boolean)


    def __init__(self, phone, email, person, auth):
        self.phone = phone
        self.email = email
        self.person = person
        self.auth = auth