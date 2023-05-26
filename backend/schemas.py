from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str
    genre_id: int


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class GenreBase(BaseModel):
    title: str
    description: str


class Genre(GenreBase):
    id: int
    movies: list[Movie] = []

    class Config:
        orm_mode = True
