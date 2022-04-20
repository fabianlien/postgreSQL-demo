from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()

class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer,  primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

#table = session.query(Artist).filter_by(ArtistId=51)
#for t in table:
#    print(t.ArtistId, t.Name, sep=" | ")

#table = session.query(Album).filter_by(ArtistId=51)
#for i in table:
#    print(i.AlbumId, i.Title, i.ArtistId, sep=" | ")

table = session.query(Track).filter_by(Composer="Queen")
for i in table:
    print(i.TrackId, i.Name, i.AlbumId,
          i.MediaTypeId, i.GenreId, i.Composer,
          i.Milliseconds, i.Bytes, i.UnitPrice, sep=" | ")