from django.db import models
from requests import request

# Create your models here.
class Movie(object):


    def __init__(self, movieTitle, genre, media ):
        self.movieTitle = movieTitle
        self.genre = genre
        self.media = media
        #self.img = img

    @classmethod
    def createMovie(self, movieTitle, genre, media ):
        _movies=[Movie(movieTitle,genre,media)]
        return '%s'%(_movies[0].movieTitle)

    def getMovieList():
        _movies = []
