from django.contrib import admin
from .models import Post, Location, Feature, Star
# Register your models here.

admin.site.register(Post)
admin.site.register(Location)
admin.site.register(Feature)
admin.site.register(Star)