from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField()
    area = models.CharField(max_length=30, null=True)
    user = models.ManyToManyField(User, blank=True)

    def total_likes(self):
        return self.user.count()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

        


class Comment(models.Model):
    comment = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField('date published', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment
