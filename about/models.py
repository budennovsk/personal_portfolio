from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title

