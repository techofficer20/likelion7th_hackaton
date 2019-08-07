from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 20)
    tag_body = models.TextField(max_length = 100)
    location = models.CharField(max_length = 15)
    def __str__(self):
        return self.title