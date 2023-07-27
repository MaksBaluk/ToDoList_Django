from django import forms
from ToDoList.models import ToDoList
from .models import CustomUser


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title', 'description', 'is_complete', 'is_private')