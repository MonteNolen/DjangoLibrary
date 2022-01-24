# Generated by Django 4.0 on 2022-01-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_alter_tags_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noteinstance',
            name='status',
        ),
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.CharField(blank=True, choices=[('В работе', 'В работе'), ('Выполнил', 'Выполнил'), ('Отложено', 'Отложено'), ('Открыто', 'Открыто')], default='Открыто', help_text='Статус задачи', max_length=10),
        ),
    ]