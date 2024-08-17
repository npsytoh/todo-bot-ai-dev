from django import forms
from .models import TodoItems


class TodoCreateModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TodoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        exclude = ['is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
