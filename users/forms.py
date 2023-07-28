from django import forms
from ToDoList.models import ToDoList


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title', 'description', 'is_complete', 'is_private')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'cols': 40, 'rows': 3}),
        }

