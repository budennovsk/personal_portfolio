from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

