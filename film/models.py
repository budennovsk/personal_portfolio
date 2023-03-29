from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.shortcuts import reverse


class Actor(models.Model):
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.first_name

class Film(models.Model):
    film = models.CharField("Фильм", blank=True, max_length=100)
    raiting = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField("Слаг", unique=True, max_length=50, db_index=True)
    actors = models.ManyToManyField(Actor, blank=True)

    def __str__(self):
        return self.film

    def get_absolute_url(self):
        return reverse('detailfilms', kwargs={'film_slug': self.slug})

    class Meta:
        ordering = ['film', 'created']