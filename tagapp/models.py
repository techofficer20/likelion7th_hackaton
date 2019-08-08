from django.db import models

# Create your models here.
from taggit.managers import TaggableManager
from taggit.models import (
    TagBase, TaggedItemBase
)


class PostTag(TagBase):
    # NOTE: django-taggit does not allow unicode by default.
    slug = models.SlugField(
        verbose_name=('slug'),
        unique=True,
        max_length=100,
        allow_unicode=True,
    )

    class Meta:
        verbose_name = ("tag")
        verbose_name_plural = ("tags")

    def slugify(self, tag, i=None):
        return default_slugify(tag, allow_unicode=True)


class TaggedPost(TaggedItemBase):
    content_object = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
    )

    tag = models.ForeignKey(
        'PostTag',
        related_name="%(app_label)s_%(class)s_items",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = ("tagged post")
        verbose_name_plural = ("tagged posts")


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    tags = TaggableManager(
        verbose_name=('tags'),
        help_text=('A comma-separated list of tags.'),
        blank=True,
        through=TaggedPost,
    )
