from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from base import Base

class Component(Base):
    __tablename__ ='component'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    img_link = Column(String)
    price = Column(Integer)


    def __init__(self, name, description, quantity, img_link, price):
        self.name = name
        self.description = description
        self.img_link = img_link
        self.quantity= quantity
        self.price = price