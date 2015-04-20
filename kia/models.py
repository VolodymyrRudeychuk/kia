import uuid
from django.contrib.auth.models import User
from django.db import models


class Front(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Token(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.token)


class Statistic(models.Model):
    token = models.ForeignKey('Token')
    access_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    title = models.CharField(max_length='50')

    def __unicode__(self):
        return self.title


class Media(models.Model):
    TYPES = (
        (1, 'English'),
        (2, 'French'),
        (3, 'Video'),
        (4, 'Audio'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(Category)
    type = models.IntegerField(choices=TYPES)

    def __unicode__(self):
        return self.name