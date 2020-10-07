from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# The user model, created by Jackson Detke
class IMDBUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    # Need clarification on what this is.
    following = models.ManyToManyField("self", symmetrical=False)

    # Shows the username instead of the ID when listing each user
    def __str__(self):
        return self.username
