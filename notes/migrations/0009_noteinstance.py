# Generated by Django 4.0 on 2022-01-24 11:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_rename_task_tags_alter_tags_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный ID для этой задачи', primary_key=True, serialize=False)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('В работе', 'В работе'), ('Выполнил', 'Выполнил'), ('Отложено', 'Отложено'), ('Открыто', 'Открыто')], default='Открыто', help_text='Статус задачи', max_length=10)),
                ('note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.note')),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.user')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]
