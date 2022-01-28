from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from datetime import date

#############################################################
    #Создание модели пользователя на основа встроенной модели
#############################################################
# class Author(models.Model):
#     """
#     Модель представляющая автора.
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

#     POSITION = [
#         ("Operator", "Оператор"),
#         ("Admin", "Администратор"),
#         ("Engineer", "Ведущий инженер"),
#     ]
#     post = models.CharField("Должность", max_length=10, choices=POSITION, blank=True, default='Operator')

#     def get_absolute_url(self):
#         """
#         Возвращает url для доступа к определенному экземпляру автора.
#         """
#         return reverse('user-detail', args=[str(self.id)])


#     def __str__(self):
#         """
#         Строка представляющая модель объекта.
#         """
#         return '{0} {1}'.format (self.last_name, self.first_name)

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

class Tags(models.Model):
    """
    Модель представляющая вид задачи
    """
    name = models.CharField("Тег", max_length=200, help_text="Введите название задачи")

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Note(models.Model):
    """
    Модель для представления формы отчета
    """
    title = models.CharField("Заголовок", max_length=100)
    user = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Ответственный')
    date = models.DateField("Дата создания",null=True, blank=True)
    textarea = models.TextField("Поле для отчета", max_length=1000)

    tags = models.ManyToManyField(Tags, help_text="Выберите тэг", blank=True, verbose_name='Теги')

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])

    def display_tags(self):
        return ', '.join([ tags.name for tags in self.tags.all() ]) #all()[:3] для вывода определнного кол-ва ])
        
    display_tags.short_description = 'Теги'

    
class NoteInstance(models.Model):
    """
    Модель представляющая копию поставленной задачи
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный ID для этой задачи")
    note = models.ForeignKey('Note', on_delete=models.SET_NULL, null=True)
    must_do = models.DateField("Выполнить до", null=True, blank=True)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('В работе', 'В работе'),
        ('Выполнил', 'Выполнил'),
        ('Отложено', 'Отложено'),
        ('Открыто', 'Открыто'),
    )
    
    status = models.CharField(max_length=10, choices=LOAN_STATUS, blank=True, default='Открыто', help_text='Статус задачи', verbose_name='Статус')

    @property
    def is_overdue(self):
        if self.must_do and date.today() > self.must_do:
            return True
        return False

    class Meta:
        ordering = ["must_do"]

        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        permissions = (("can_mark_returned", "Что-то должно тут быть"),)

    def __str__(self):
        return '{0} {1}'.format (self.id, self.note.title)

