from django.contrib import admin

# Register your models here.
from django.shortcuts import render
from .models import Movie

def movie_list(request):
    genre_filter = request.GET.getlist('genre')
    title_search = request.GET.get('title', '')

    movies = Movie.objects.all()

    if genre_filter:
        movies = movies.filter(genres__icontains=genre_filter)

    if title_search:
        movies = movies.filter(title__icontains=title_search)

    context = {
        'movies': movies,
        'genre_filter': genre_filter,
        'title_search': title_search,
    }

    return render(request, 'movies/movie_list.html', context)
