from django import forms
from .models import TodoItems


class TodoCreateModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }