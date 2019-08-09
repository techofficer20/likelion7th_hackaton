from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 20)
    location = models.CharField(max_length = 10)
    feature = models.CharField(max_length = 20)
    description = models.TextField(max_length = 1000)
    
    def __str__(self):
        return self.title
