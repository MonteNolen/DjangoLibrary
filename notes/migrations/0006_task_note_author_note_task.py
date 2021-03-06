# Generated by Django 4.0 on 2022-01-24 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_user_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название задачи', max_length=200, verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.user'),
        ),
        migrations.AddField(
            model_name='note',
            name='task',
            field=models.ManyToManyField(help_text='Выберите вид задачи', to='notes.Task'),
        ),
    ]
