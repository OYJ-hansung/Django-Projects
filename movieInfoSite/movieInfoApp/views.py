from django.shortcuts import render
from movieInfoApp.models import Movie
from movieInfoApp.forms import movieForm

def index(request):
    return render(request, 'movieInfoApp/index.html')

def listMovies(request):
    movieList = Movie.objects.all()
    return render(request, 'movieInfoApp/moviesList.html', {'movies':movieList})

def addMovie(request):
    form = movieForm(request.POST)
    if form.is_valid():
        form.save()
        return index(request)
    return render(request, 'movieInfoApp/newMovie.html', {'form': form})