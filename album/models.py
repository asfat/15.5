from django.db import models
from musician.models import Musician
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Album(models.Model):
    albumName=models.CharField(max_length=30)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE)
    release_date=models.DateField(blank=True,null=True)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        default=0
    )
    def __str__(self):
        return self.albumName