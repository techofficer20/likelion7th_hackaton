# Generated by Django 2.2.3 on 2019-08-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0014_auto_20190809_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='feature',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
