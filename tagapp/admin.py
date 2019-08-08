from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models

from .models import TaggedPost
from .models import PostTag
from .models import Post

admin.site.register(Post)
admin.site.register(TaggedPost)
admin.site.register(PostTag)

