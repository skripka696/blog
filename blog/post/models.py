from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name="children", db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name="children", db_index=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title