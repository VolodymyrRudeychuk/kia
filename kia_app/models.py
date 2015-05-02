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
    user = models.ForeignKey(User, related_name='tkn')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.token)


class Statistic(models.Model):
    token = models.ForeignKey('Token')
    access_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):

    TYPES = (
        (1, 'Video'),
        (2, 'Audio'),

    )

    LANGUAGES = (
        (1, 'English'),
        (2, 'French'),
    )

    GRADES = (
        (0, 'Kindergarten (ages 4-5)'),
        (1, 'Grade 1'),
        (2, 'Grade 2'),
        (3, 'Grade 3'),
        (4, 'Grade 4'),
        (5, 'Grade 5'),
        (6, 'Grade 6'),
        (7, 'Grade 7'),
        (8, 'Grade 8'),
        (9, 'Grade 9'),
    )

    title = models.CharField(max_length='50')
    grade = models.IntegerField(choices=GRADES)
    type = models.IntegerField(choices=TYPES)
    language = models.IntegerField(choices=LANGUAGES)

    def __unicode__(self):
        return self.title


class Media(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name