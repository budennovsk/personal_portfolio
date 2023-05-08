from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from .models import Actor, Film


def listfilms(request: object) -> render:
    """ Отображения списка всех фильмов"""
    films = Film.objects.all()
    return render(request, 'film/listfilms.html', {'films': films})


def detailfilms(request: object, film_slug: str) -> render:
    """ Отображения списка актеров"""
    actors = Film.objects.filter(slug=film_slug).prefetch_related('actors')

    context = {

        'actors': actors,
    }
    return render(request, 'film/detailfilms.html', context=context)
