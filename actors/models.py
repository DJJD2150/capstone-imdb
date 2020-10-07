from django.db import models
from movies.models import Movies

# Create your models here.
# The actor model, created by Jackson Detke
class Actors(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()
    # Note:  Add upload photo folder later.
    photo = models.ImageField(null=True, blank=True)
    filmography = models.ForeignKey(Movies, on_delete=models.CASCADE)

    # Shows the title instead of the ID when listing each actor
    def __str__(self):
        return self.name