from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    body = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
