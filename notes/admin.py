from django.contrib import admin
from .models import Note, Tags, NoteInstance, UsersPro #, User

admin.site.register(Tags)

class Notes(admin.TabularInline):
    model = Note
    extra = 0

class UsersProAdmin(admin.ModelAdmin):
    #list_display = ('first_name', 'last_name')    # декорация списка
    #fields = ['first_name', 'last_name']        # декорация списка
    inlines = [Notes]   # выводим отображение связанной модели

admin.site.register(UsersPro, UsersProAdmin)

class NoteInstanceInline(admin.TabularInline):
    model = NoteInstance
    extra = 0

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('status', 'tags')
    list_display = ('title',  'status', 'display_tags') #'user',
    inlines = [NoteInstanceInline]

@admin.register(NoteInstance)
class NoteInstanceAdmin(admin.ModelAdmin):
    list_display = ('note', id, 'due_back', 'responsible')
    fieldsets = (
        (None, { 
            'fields': ('note', 'id')
        }),
        ('Availability', {
            'fields': ('due_back', 'responsible')
        }),
    )
