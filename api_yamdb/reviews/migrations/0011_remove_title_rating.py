# Generated by Django 3.2 on 2023-05-18 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_title_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]
