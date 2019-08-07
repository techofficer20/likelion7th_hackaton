from django.db import models

# Create your models here.
one_to_five_chocies = zip(range(1,5+1), range(1,5+1))

class Post(models.Model):
    title = models.CharField(max_length = 20)
    tag_body = models.TextField(max_length = 100)
    location = models.CharField(max_length = 15)
    starrate = models.SmallIntegerField(choices=one_to_five_chocies, default=3)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-starrate']    

