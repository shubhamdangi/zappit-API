from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
