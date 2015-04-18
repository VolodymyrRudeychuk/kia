from django.db import models


class Front(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


# class Message(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(blank=True)
#     phone = models.CharField(max_length=15)
#     message = models.TextField(blank=True)
#     date = models.DateTimeField(auto_now_add=True)