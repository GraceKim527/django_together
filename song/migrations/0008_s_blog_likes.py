# Generated by Django 3.2.9 on 2021-11-05 07:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('song', '0007_auto_20211029_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_blog',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
