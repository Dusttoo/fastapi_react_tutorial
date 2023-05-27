from sqlalchemy.orm import Session
from models import Genre, Movie
from schemas import GenreBase, MovieBase


def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def get_movie_by_title(db: Session, title: str):
    return db.query(Movie).filter(Movie.title == title).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: MovieBase):
    db_movie = Movie(title=movie.title,
                     description=movie.description, genre_id=movie.genre_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()


def get_genre_by_title(db: Session, title: str):
    return db.query(Genre).filter(Genre.title == title).first()


def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Genre).offset(skip).limit(limit).all()


def create_genre(db: Session, genre: GenreBase):
    db_genre = Genre(title=genre.title, description=genre.description)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre
