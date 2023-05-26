from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

    movies = relationship("Movie", back_populates="genre")


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    genre_id = Column(Integer, ForeignKey("genres.id"))

    genre = relationship("Genre", back_populates="movies")
