# Generated by Django 3.0.5 on 2021-09-16 15:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20210916_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbs',
            field=models.ManyToManyField(blank=True, default=None, related_name='thumbs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbsdown',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbsup',
            field=models.IntegerField(default='0'),
        ),
    ]
