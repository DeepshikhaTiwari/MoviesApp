from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.MovieList.as_view(), name='movies'),
    path('movie/<int:pk>', views.MovieDetail.as_view(), name='movie-detail'),
    path('movie/create', views.MovieCreate.as_view(), name='movie-create'),

    path('directors/', views.DirectorList.as_view(), name='directors'),
    path('director/<int:pk>', views.DirectorDetail.as_view(), name='director-detail'),
    path('director/create', views.DirectorCreate.as_view(), name='director-create'),

    path('genres/', views.GenreList.as_view(), name='genres'),
    path('genre/<int:pk>', views.GenreDetail.as_view(), name='genre-detail'),

    path('studios/', views.StudioList.as_view(), name='studios'),
    path('studio/<int:pk>', views.StudioDetail.as_view(), name='studio-detail'),
    path('stduio/create', views.StudioCreate.as_view(), name='studio-create'),

]
