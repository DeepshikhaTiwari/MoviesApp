from django.shortcuts import render
from .models import director, Genre, Movie, studio
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'index.html')


class MovieList(ListView):
    model = Movie
    template_name = "movie_list"
    context_object_name = "movies"


class MovieDetail(DetailView):
    model = Movie


class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'slug', 'directors', 'studio', 'genre', 'movie_url', 'img_url', 'asin']


class DirectorList(ListView):
    model = director
    template_name = "director_list"
    context_object_name = "directors"


class DirectorDetail(DetailView):
    model = director


class DirectorCreate(CreateView):
    model = director
    fields = ['name', 'phone_no', 'dob', 'website', 'profile_url', 'gender']


class StudioList(ListView):
    model = studio
    template_name = "studio_list"


class StudioDetail(DetailView):
    model = studio


class StudioCreate(CreateView):
    model = studio
    fields = ['title', 'website', 'slug']


class GenreList(ListView):
    model = Genre
    template_name = "genre_list"
    context_object_name = "genres"


class GenreDetail(DetailView):
    model = Genre
