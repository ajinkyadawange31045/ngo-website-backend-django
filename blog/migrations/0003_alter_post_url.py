# Generated by Django 5.1.1 on 2024-09-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_author_remove_post_bookmark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
