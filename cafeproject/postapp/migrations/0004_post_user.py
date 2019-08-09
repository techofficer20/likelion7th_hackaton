# Generated by Django 2.2.3 on 2019-08-09 07:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postapp', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]