# Generated by Django 5.0 on 2023-12-16 19:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='saved_by',
            field=models.ManyToManyField(related_name='saved_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]