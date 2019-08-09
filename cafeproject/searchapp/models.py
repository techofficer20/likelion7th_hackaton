from django.db import models

# Create your models here.
one_to_five_chocies = zip(range(1,5+1), range(1,5+1))

class Location(models.Model):
    location = models.CharField(max_length = 10)

    def __str__(self):
        return self.location

class Feature(models.Model):
    feature = models.CharField(max_length = 15)
    
    def __str__(self):
        return self.feature

class Post(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField(max_length = 1000)
    feature = models.ForeignKey(Feature, on_delete = models.CASCADE)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    starrate = models.SmallIntegerField(choices=one_to_five_chocies, default=3)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-starrate']    

class Star(models.Model):
    star = models.CharField(max_length = 3)

    def __str__(self):
        return self.star