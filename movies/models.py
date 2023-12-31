from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

STAR_RATING = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]


class Movie(models.Model):
    name = models.CharField(max_length=80)
    rating = models.IntegerField(choices=STAR_RATING)
    director = models.CharField(max_length=20)
    duration = models.IntegerField(validators=[ MinValueValidator(1, message="Invalid duration time") ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
