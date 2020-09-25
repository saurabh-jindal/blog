from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    message = models.TextField()
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images/', default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "New post added with message: " + self.message + " by user " + self.user.username





    