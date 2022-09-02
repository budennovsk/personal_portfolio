from django.shortcuts import render
from .models import About

def all_about(request):
    abouts = About.objects.all()
    return render(request, 'about/all_about.html', {'abouts': abouts})
