from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import Base, Genre, Movie
from schemas import Genre, GenreBase, Movie, MovieBase
from crud import get_genre_by_title, get_genres, get_movie, get_movie_by_title, get_movies
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/movies/", response_model=Movie)
def create_movie(movie: MovieBase, db: Session = Depends(get_db)):
    db_movie = get_movie_by_title(db, title=movie.title)
    if db_movie:
        raise HTTPException(status_code=400, detail="Movie already exists")
    return create_movie(db=db, movie=movie)


@app.get("/movies/", response_model=list[Movie])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = get_movies(db, skip=skip, limit=limit)
    return movies


@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@app.get("/genres/", response_model=list[Genre])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genres = get_genres(db, skip=skip, limit=limit)
    return genres


@app.post("/genres/", response_model=Genre)
def create_genre(genre: GenreBase, db: Session = Depends(get_db)):
    db_genre = get_genre_by_title(db, title=genre.title)
    if db_genre:
        raise HTTPException(status_code=400, detail="Genre already exists")
    return create_genre(db=db, genre=genre)
