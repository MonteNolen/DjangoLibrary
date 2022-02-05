from django.contrib import admin
from .models import Note, Task, Author

class Tasks(admin.TabularInline):
    model = Task
    extra = 0

class Notes(admin.TabularInline):
    model = Note
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    inlines = [Notes, Tasks]

admin.site.register(Author, AuthorAdmin)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('user', 'date')
    list_display = ('title', 'user', 'date')
    #inlines = [TaskInline]
    fieldsets = (
        # (None, { 
        #     'fields': ('note', 'id')
        # }),
        ('Availability', {
            'fields': ('title', 'user', 'textarea')
        }),
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter= ('status', 'responsible')
    list_display = ('user', 'title', 'created', 'status', 'responsible')
    search_fields = ['title', 'textarea']
    fieldsets = (
        # (None, { 
        #     'fields': ('note', 'id')
        # }),
        ('Availability', {
            'fields': ('user', 'title', 'status', 'closed', 'responsible', 'textarea')
        }),
    )
