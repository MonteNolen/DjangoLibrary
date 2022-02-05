# Generated by Django 4.0 on 2022-02-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['created'], 'permissions': (('can_mark_returned', 'Что-то должно тут быть'),), 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='must_do',
        ),
        migrations.AddField(
            model_name='task',
            name='closed',
            field=models.DateField(blank=True, null=True, verbose_name='Создано'),
        ),
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateField(auto_now=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('Выполнено', 'Выполнено'), ('Открыто', 'Открыто')], default='Открыто', help_text='Статус задачи', max_length=10, verbose_name='Статус'),
        ),
    ]