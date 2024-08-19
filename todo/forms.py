from django import forms
from .models import TodoItems


class TodoCompletedModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = ['is_completed']
        widgets = {
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            })
        }

class TodoCreateModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'タスクを入力...',
            }),
        }

class TodoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        exclude = ['is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'メモを入力...',
            }),
        }
