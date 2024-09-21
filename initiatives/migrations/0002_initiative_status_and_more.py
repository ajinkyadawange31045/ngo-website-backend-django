# Generated by Django 5.1.1 on 2024-09-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiative',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='tags_for_seo_and_search_bar_in_website',
            field=models.TextField(help_text='Add tags for search and SEO purposes.'),
        ),
    ]
