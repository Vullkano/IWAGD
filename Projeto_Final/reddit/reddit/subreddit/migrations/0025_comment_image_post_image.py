# Generated by Django 4.1 on 2023-10-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0024_reddituser_following_alter_reddituser_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]