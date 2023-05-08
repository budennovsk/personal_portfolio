from django.shortcuts import render
from .models import Project


def home(request: object) -> render:
    """ Отображения домашней страницы"""
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

