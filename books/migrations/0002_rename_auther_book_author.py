# Generated by Django 4.0 on 2023-10-22 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='auther',
            new_name='author',
        ),
    ]
