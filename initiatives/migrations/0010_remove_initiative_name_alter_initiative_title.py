# Generated by Django 5.1.1 on 2024-09-28 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0009_initiative_youtube_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initiative',
            name='name',
        ),
        migrations.AlterField(
            model_name='initiative',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
