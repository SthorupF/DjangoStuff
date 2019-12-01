from django.shortcuts import HttpResponse
from .movie import Movie
from django.shortcuts import render
# Create your views here.
from .forms.createMovieForm import CreateMovieForm
def index(request):

    if request.method=='POST':
        form = CreateMovieForm(request.POST)

        if form.is_valid():
            return HttpResponse(Movie.createMovie(form.cleaned_data['movieTitle'],form.cleaned_data['genre'],form.cleaned_data['media']))
    else:
        form=CreateMovieForm()

    return render(request, 'templates/template.html', {'form':form})

#def get(self):
#    movie = models.GetMovie('tt3896198', self);
#    return movie
