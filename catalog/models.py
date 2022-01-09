from django.db import models
from django.urls import reverse
import uuid # Требуется для уникальных экземпляров книг

class Genre(models.Model):
    """
    Модель представляющая жанр книги (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Введите жанр книги")

    def __str__(self):
        """
        Строка для представления модели объекта (в Админ панеле etc.)
        """
        return self.name

class Book(models.Model):
    """
    Модель представляющая книгу (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)  # null=True, позволяет базе данных хранить значение Null, если автор не выбран
                                                                                # on_delete = models.SET_NULL установит значение автора в Null, если связанная с автором запись будет удалена
    # Foreign Key используется потому что, книга имеет одного автора, но автор имеет множество книг
    # Author в виде строки, а не объекта, потому что он еще не был объявлен в файле.
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 символов <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр для книги")
    # ManyToManyField используется потому что жанр может использоваться в многих книгах. Книги могут охватывать множество жанров.
    # Genre класс уже определен, поэтому мы можем указать объект выше.

    def __str__(self):
        """
        Строка для представления модели объекта.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.book.title)