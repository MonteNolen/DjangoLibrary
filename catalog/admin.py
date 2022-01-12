from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)

class Books(admin.TabularInline):
    model = Book    # берем модель для отображения в связуемом классе
    extra = 0       # убирает лишнии дополнительные поля для связанных книг

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')    # декорация списка
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]        # декорация списка
    inlines = [Books]   # выводим отображение связанной модели

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # убирает лишнии дополнительные поля для связанных книг

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', id, 'status', 'due_back')
    fieldsets = (
        (None, { 
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



