from django.db import models
from django.contrib.auth.models import User
from actors.models import Actors

# Create your models here.
# The movie model, created by Jackson Detke
class Movies(models.Model):
    title = models.CharField(max_length=80)
    director = models.CharField(max_length=50)
    description = models.TextField()
    # Note:  DateField properties???
    release_date = models.DateField()
    # What was the "instructions" part of the Movie model in Leanne's version of the capstone?
    # Note:  Add upload photo folder later.
    photo = models.ImageField(null=True, blank=True)
    actors = models.ForeignKey(Actors, on_delete=models.CASCADE, default=True)
    genre = models.TextField()

    # Shows the title instead of the ID when listing each movie
    def __str__(self):
        return self.title