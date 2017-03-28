from django.db import models
from django.contrib.auth.models import AbstractUser
from post.models import Post


class User(AbstractUser):
    favorites = models.ManyToManyField(Post, blank=True, null=True)
