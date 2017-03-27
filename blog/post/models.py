from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name="children", db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Models):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category)
    tag = models.ForeignKey(Tag)


class Comment(models.Model):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name="children", db_index=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')