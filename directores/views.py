from django.shortcuts import render
from models import Director, Movies


def index(request):
    directors = Director.objects.all().count()
    movies = Movies.objects.all().count()


