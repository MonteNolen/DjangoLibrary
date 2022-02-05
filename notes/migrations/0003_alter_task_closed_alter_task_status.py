# Generated by Django 4.0 on 2022-02-05 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_task_options_remove_task_must_do_task_closed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='closed',
            field=models.DateField(blank=True, null=True, verbose_name='Закрыто'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('Закрыт', 'Закрыт'), ('Открыт', 'Открыт')], default='Открыто', help_text='Статус задачи', max_length=10, verbose_name='Статус'),
        ),
    ]
