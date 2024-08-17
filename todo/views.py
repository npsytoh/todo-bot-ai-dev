from django.urls import reverse_lazy
from django.views import generic

from .models import TodoItems
from .forms import TodoCreateModelForm


class TodoMainView(generic.ListView, generic.edit.ModelFormMixin):
    model = TodoItems
    form_class = TodoCreateModelForm
    template_name = 'todo/todo-main.html'
    context_object_name = 'todo_lists'
    success_url = reverse_lazy('todo-main')

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)