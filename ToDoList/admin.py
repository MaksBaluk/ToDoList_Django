from django.contrib import admin
from .models import ToDoList


# Register your models here.
@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    model = ToDoList
    list_display_links = ['title', 'slug', 'updated_at']
    list_display = ['title', 'slug', 'updated_at', 'is_complete', 'is_private']
    list_editable = ('is_complete','is_private')
    ordering = ['updated_at']
    fieldsets = [
        (
            'ToDoList',
            {
                "fields": ["title", "description", "is_complete", "is_private"],
            },
        ),
    ]


