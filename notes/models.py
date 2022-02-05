from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from datetime import date

class Author(models.Model):
    """
    Модель представляющая автора.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


    def __str__(self):
        return self.user.get_full_name()

class Note(models.Model):
    """
    Модель для представления отчета
    """
    title = models.CharField("Заголовок", max_length=100)
    user = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')
    date = models.DateField("Дата", auto_now_add=True)
    textarea = models.TextField("Поле для отчета", max_length=1000)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])

class Task(models.Model):
    """
    Модель представляющая задачу
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный ID для этой задачи")
    user = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')
    title = models.CharField("Заголовок", max_length=100)
    created = models.DateField("Создана", auto_now=True)
    closed = models.DateField("Закрыта", null=True, blank=True)
    textarea = models.TextField("Текст задачи", max_length=1000)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    STATUS_CHOICES =(
        ('Закрыт', 'Закрыт'),
        ('Открыт', 'Открыт'),
)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True, default='Открыто', help_text='Статус задачи', verbose_name='Статус')

    @property
    def is_overdue(self):
        if self.created and date.today() > self.created:
            return True
        return False

    class Meta:
        ordering = ["created"]
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        permissions = (("can_mark_returned", "Что-то должно тут быть"),)

    def __str__(self):
        return '{0} {1}'.format (self.id, self.title)

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)])

