
from django.urls import path

from . import views

urlpatterns = [

    # Auth
    path('signup/', views.signupuser, name="signupuser"),
    path('logout/', views.logoutuserr, name="logoutuserr"),
    path('login/', views.loginuser, name="loginuser"),
    # Todos
    path('current/', views.currenttodos, name="currenttodos"),
    path('', views.home, name="home"),
    path('create/', views.createtodo, name="createtodo"),
    path('todo/<int:todo_pk>', views.viewtodo, name="viewtodo"),
    path('todo/<int:todo_pk>/complete', views.completetodo, name="completetodo"),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name="deletetodo"),
    path('completed', views.completedtodos, name="completedtodos"),
]
