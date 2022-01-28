from django.contrib import admin
from .models import Note, Tags, NoteInstance, Author

admin.site.register(Tags)

class Notes(admin.TabularInline):
    model = Note
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    #list_display = ('user', 'post')    # декорация списка
    inlines = [Notes]   # выводим отображение связанной модели

admin.site.register(Author, AuthorAdmin)

class NoteInstanceInline(admin.TabularInline):
    model = NoteInstance
    extra = 0

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    #list_filter = ('status', 'tags')
    list_display = ('title', 'display_tags', 'user') #'user',
    inlines = [NoteInstanceInline]

@admin.register(NoteInstance)
class NoteInstanceAdmin(admin.ModelAdmin):
    list_display = ('note', id, 'must_do', 'status', 'responsible')
    fieldsets = (
        (None, { 
            'fields': ('note', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'must_do', 'responsible')
        }),
    )
