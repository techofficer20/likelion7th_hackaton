from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField()
    area = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
