
from django.shortcuts import render, get_object_or_404
from .models import Actor, Film


def listfilms(request):

    films = Film.objects.all()
    return render(request, 'film/listfilms.html', {'films': films})

def detailfilms(request, film_slug):
    posts = get_object_or_404(Film, slug=film_slug)
    actors = Actor.objects.all()
    context = {
        'posts': posts,
        'actors': actors,
    }
    return render(request, 'film/detailfilms.html', context=context)

