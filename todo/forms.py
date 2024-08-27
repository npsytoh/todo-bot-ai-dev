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

class TodoEditModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.base_fields['is_important'].initial = True
        super().__init__(*args, **kwargs)

    class Meta:
        model = TodoItems
        exclude = [
            'task_id',
            'completed_at'
        ]
        widgets = {
            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'task_title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'task_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'メモを入力...',
            }),
            'is_important': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select',
            }),
            'due_date': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }
