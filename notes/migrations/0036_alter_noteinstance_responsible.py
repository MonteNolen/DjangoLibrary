# Generated by Django 4.0 on 2022-01-25 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0035_alter_author_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteinstance',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.author'),
        ),
    ]
