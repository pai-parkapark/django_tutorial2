from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Upload(models.Model):
    file = models.FileField()