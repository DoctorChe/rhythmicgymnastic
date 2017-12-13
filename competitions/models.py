from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Competition(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Apparatus(models.Model):
    owner = models.ForeignKey(User, related_name='apparatus_created', on_delete=models.DO_NOTHING)
    competition = models.ForeignKey(Competition, related_name='apparatuses', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Group(models.Model):
    apparatus = models.ForeignKey(Apparatus, related_name='groups', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Gymnast(models.Model):
    group = models.ForeignKey(Group, related_name='gymnasts', on_delete=models.DO_NOTHING)
    gymnast_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('gymnast_type', 'object_id')