from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship

from Movies.domainmodel.user import User
from Movies.domainmodel.review import Review
from Movies.domainmodel.movie import Movie

metadata = MetaData()


# just need users, movies, and reviews
# remember that users, movies, and reviews link so relation will need to be established
# keep
users = Table(
    'users', metadata,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)
# keep
reviews = Table(
    'review', metadata,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('username', ForeignKey('users.username'), nullable=False),
    Column('movie_id', ForeignKey('movies.Rank'), nullable=False),
    Column('review', String(1024), nullable=False),
    Column('rating', Integer, nullable=False)
)
# keep
movies = Table(
    'movies', metadata,
    Column('Rank', Integer, primary_key=True, autoincrement=True),
    Column('Title', String(255), nullable=False),
    Column('Genre', String(255), nullable=False),
    Column('Description', String(1024), nullable=False),
    Column('Director', String(255), nullable=False),
    Column('Actors', String(1024), nullable=False),
    Column('Year', String(255), nullable=False),
    Column('Runtime', String(255), nullable=False),
    Column('Rating', String(255), nullable=False),
    Column('Votes', String(255), nullable=False),
    Column('Revenue', String(255), nullable=False),
    Column('Metascore', String(255), nullable=False)
)


# dont really understand this.
# maps the domain variables to database?
"""Object relational mapper: the SQLAlchemymapper function maps domain model objectsto the created tables, 
and deals with associations (relationships). All strings in the mapper (_comments, _user) are actually variables in 
the domain model classes!"""


# TODO
def map_model_to_tables():

    mapper(User, users, properties={
        '_username': users.c.username,
        '_password': users.c.password,
        # not sure about how backref works
        '_reviews': relationship(Review, backref='_username')
    })

    mapper(Review, reviews, properties={
        '_user': reviews.c.username,
        '_movie': reviews.c.movie_id,
        '_review_text': reviews.c.review,
        '_rating': reviews.c.rating
    })

    mapper(Movie, movies, properties={
        '_title': movies.c.Title,
        '_release': movies.c.Year,
        'description': movies.c.Description,
        '_director': movies.c.Director,
        '_actors': movies.c.Actors,
        '_genres': movies.c.Genre,
        '_runtime_minutes': movies.c.Runtime
    })


'''
comments = Table(
    'comments', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id')),
    Column('article_id', ForeignKey('articles.id')),
    Column('comment', String(1024), nullable=False),
    Column('timestamp', DateTime, nullable=False)
)

articles = Table(
    'articles', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('date', Date, nullable=False),
    Column('title', String(255), nullable=False),
    Column('first_para', String(1024), nullable=False),
    Column('hyperlink', String(255), nullable=False),
    Column('image_hyperlink', String(255), nullable=False)
)

tags = Table(
    'tags', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(64), nullable=False)
)

article_tags = Table(
    'article_tags', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('article_id', ForeignKey('articles.id')),
    Column('tag_id', ForeignKey('tags.id'))
)
'''