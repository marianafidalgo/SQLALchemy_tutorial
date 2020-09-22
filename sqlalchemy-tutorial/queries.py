#1. Imports
from actor import Actor
from datetime import date
from base import Session
from contact_details import ContactDetails
from movie import Movie

#2. Extract a session
session = Session()

#3. Extract all movies
movies = session.query(Movie).all()

#4. Print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

#5. Get movies after 15-01-01
movies = session.query(Movie) \
    .filter(Movie.release_date > date(2015,1,1)) \
    .all()

print('### Recent movies:')

for movie in movies:
    print(f'{movie.title} was released after 2015')
print('')

# 6. Movies that Dwayne Johnson participated
the_rock_movies = session.query(Movie) \
    .join(Actor, Movie.actors) \
    .filter(Actor.name == 'Dwayne Johnson') \
    .all()

print('### Dwayne Johnson movies:')
for movie in the_rock_movies:
    print(f'The Rock starred in {movie.title}')
print('')

# 7. Get actors that have house in Glendale
glendale_stars = session.query(Actor) \
    .join(ContactDetails) \
    .filter(ContactDetails.address.ilike('%glendale%')) \
    .all()

print('### Actors that live in Glendale:')
for actor in glendale_stars:
    print(f'{actor.name} has a house in Glendale')
print('')