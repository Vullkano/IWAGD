# Generated by Django 4.2.6 on 2023-10-12 16:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("subreddit", "0009_rename_total_votes_post_dislikes_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="disliked_by",
            field=models.ManyToManyField(
                blank=True, related_name="disliked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True, related_name="liked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
