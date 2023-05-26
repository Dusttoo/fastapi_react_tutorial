from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import models, schemas
from api import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=movie.title)
    if db_movie:
        raise HTTPException(status_code=400, detail="Movie already exists")
    return crud.create_movie(db=db, movie=movie)


@app.get("/movies/", response_model=list[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@app.get("/genres/", response_model=list[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genres = crud.get_genres(db, skip=skip, limit=limit)
    return genres


@app.post("/genres/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreBase, db: Session = Depends(get_db)):
    db_genre = crud.get_genre_by_title(db, title=genre.title)
    if db_genre:
        raise HTTPException(status_code=400, detail="Genre already exists")
    return crud.create_genre(db=db, genre=genre)
