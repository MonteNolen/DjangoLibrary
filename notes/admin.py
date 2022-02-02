from django.contrib import admin
from .models import Note, NoteInstance, Author

class Notes(admin.TabularInline):
    model = Note
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    inlines = [Notes]

admin.site.register(Author, AuthorAdmin)

class NoteInstanceInline(admin.TabularInline):
    model = NoteInstance
    extra = 0

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('user', 'date')
    list_display = ('title', 'user', 'date')
    inlines = [NoteInstanceInline]

@admin.register(NoteInstance)
class NoteInstanceAdmin(admin.ModelAdmin):
    list_filter= ('status', 'responsible')
    list_display = ('note', id, 'must_do', 'status', 'responsible')
    fieldsets = (
        (None, { 
            'fields': ('note', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'must_do', 'responsible')
        }),
    )
