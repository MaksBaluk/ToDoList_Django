from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from ToDoList.models import ToDoList


# Register your models here.

class ToDoListInline(admin.StackedInline):
    model = ToDoList
    extra = 0
    fieldsets = [
        (
            'ToDoList',
            {
                "fields": ["title", "description", "is_complete", "is_private"],
            },
        ),
    ]


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'slug', 'last_login', 'is_staff']
    ordering = ['last_login']
    search_fields = ['username']
    inlines = [ToDoListInline]
    fieldsets = [
        (
            'User',
            {
                "fields": ["username", "password", "slug", 'is_staff'],
            },
        ),
    ]
