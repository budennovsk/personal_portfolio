
from django.urls import path

from . import views


urlpatterns = [
    path('', views.listfilms, name='listfilms'),
    path('<slug:film_slug>/', views.detailfilms, name='detailfilms'),
]