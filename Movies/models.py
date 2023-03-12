from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    rating = models.DecimalField(decimal_places=1, max_digits=1)

    def __str__(self):
        return self.name
