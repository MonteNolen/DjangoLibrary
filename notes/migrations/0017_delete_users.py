# Generated by Django 4.0 on 2022-01-24 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0016_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='users',
        ),
    ]
