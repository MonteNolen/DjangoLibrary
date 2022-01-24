from django.contrib import admin
from .models import User, Note, Tags, NoteInstance

#admin.site.register(User)
#admin.site.register(Note)
admin.site.register(Tags)
#admin.site.register(NoteInstance)

class Notes(admin.TabularInline):
    model = Note
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'post')    # декорация списка
    fields = ['first_name', 'last_name', 'post']        # декорация списка
    inlines = [Notes]   # выводим отображение связанной модели

admin.site.register(User, UserAdmin)

class NoteInstanceInline(admin.TabularInline):
    model = NoteInstance
    extra = 0

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'display_tags')
    inlines = [NoteInstanceInline]

@admin.register(NoteInstance)
class NoteInstanceAdmin(admin.ModelAdmin):
    #list_filter = ('status', 'due_back')
    list_display = ('note', id, 'due_back', 'responsible')
    fieldsets = (
        (None, { 
            'fields': ('note', 'id')
        }),
        ('Availability', {
            'fields': ('due_back', 'responsible')
        }),
    )
