from django import forms
from .models import TodoItems


class TodoCompletedModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = ['status']
        widgets = {
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            })
        }

class TodoCreateModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = ['task_title']
        widgets = {
            'task_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'タスクを入力...',
            }),
        }

class TodoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        exclude = ['status']
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'メモを入力...',
            }),
        }
