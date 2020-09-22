#Imports
from base import Session, engine, Base
from person import Person
from contact import Contact
from team import Team
from component import Component

#Generate database schema
Base.metadata.create_all(engine)

#Create a new session
session = Session()

#Create team
one = Team("One","thing1",100)
two = Team("Two","thing2", 100)

#Create person
mariana = Person("Mariana","MEEC",22, one)
ricardo = Person("Ricardo","MEEC",23, one)
miguel = Person("Miguel","MEEC",21,two)
raquel = Person("Raquel","MEEC",18, two)

#Create components
sensor = Component("sensor", "measures things", 3, "http://sadka",10)
resistance = Component("resistance", "10ohm", 50, "http://sd",50)
arduino = Component("arduino", "microprocessor", 3, "http://fdf",2)

#Create contacts
mariana_contact = Contact(65465465, "mariana@neecist.org", mariana, True)
ricardo_contact = Contact(25241859, "ricardo@neecist.org", ricardo, False)
miguel_contact = Contact(88846546, "miguel@bosch.org", miguel, True)
raquel_contact = Contact(44715478, "raquel@bosch.org", raquel, False)


#Persists data
session.add(one)
session.add(two)

session.add(mariana)
session.add(ricardo)
session.add(miguel)
session.add(raquel)

session.add(sensor)
session.add(resistance)
session.add(arduino)

session.add(mariana_contact)
session.add(ricardo_contact)
session.add(miguel_contact)
session.add(raquel_contact)

#Commit and close session
session.commit()
session.close()