from django.db import models
from django import forms
MEDIA_CHOICE = [
    ('dvd','DVD'),
    ('blueray','BlueRay'),
    ('file','Fil'),
    ]
class CreateMovieForm(forms.Form):
    movieTitle = forms.CharField(label='Title')
    genre = forms.CharField(label='Genre')
    media = forms.CharField(label='Medie', widget=forms.Select(choices=MEDIA_CHOICE))
    #img = models.FileField(upload_to='img/')
