from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.post.models import Post


class User(AbstractUser):
    favorites = models.ManyToManyField(Post)