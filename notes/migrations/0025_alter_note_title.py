# Generated by Django 4.0 on 2022-01-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0024_alter_noteinstance_responsible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Заголовок'),
        ),
    ]
