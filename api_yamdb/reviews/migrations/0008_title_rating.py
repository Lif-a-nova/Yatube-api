# Generated by Django 3.2 on 2023-05-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_genre_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=77793),
            preserve_default=False,
        ),
    ]
