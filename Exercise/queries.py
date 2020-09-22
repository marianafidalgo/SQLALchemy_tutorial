#1. Imports
from team import Team
from person import Person
from base import Session
from contact import Contact
from component import Component

#2. Extract a session
session = Session()

#3. Extract all people
person = session.query(Person).all()

#4. Print person details
print('\n### All people:')
for p in person:
    print(p.name)
    #...
print('')
