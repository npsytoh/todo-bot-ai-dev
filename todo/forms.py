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
                'class': 'form-control shadow-sm',
                'placeholder': 'タスクを入力...',
            }),
        }

class TodoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        exclude = [
            'task_id',
            'status',
            'completed_at'
        ]
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control'}),
            'task_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'メモを入力...',
            }),
            'is_important': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'due_date': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }
