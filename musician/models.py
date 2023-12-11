from django.db import models

# Create your models here.
class Musician(models.Model):
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=11)
    instrumentType=models.TextField()

    def __str__(self):
        return self.firstName
