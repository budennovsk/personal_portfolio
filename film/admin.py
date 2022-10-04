from django.contrib import admin
from .models import *


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'raiting')
    prepopulated_fields = {"slug": ("film",)}

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')



admin.site.register(Film,FilmAdmin)
admin.site.register(Actor,ActorAdmin)
