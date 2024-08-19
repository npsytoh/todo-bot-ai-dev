from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import TodoItems
from .forms import TodoCompletedModelForm
from .forms import TodoCreateModelForm
from .forms import TodoUpdateModelForm


class TodoMainView(generic.ListView, generic.edit.ModelFormMixin):
    model = TodoItems
    form_class = TodoCreateModelForm
    template_name = 'todo/todo-main.html'
    context_object_name = 'todo_lists'
    success_url = reverse_lazy('todo-main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_item"] = TodoCompletedModelForm(self.request.POST or None)
        return context

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

class TodoCheckToggleView(generic.FormView):
    model = TodoItems
    form_class = TodoCompletedModelForm
    success_url = reverse_lazy('todo-main')
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = get_object_or_404(TodoItems, pk=pk) 
        field_name = f'is_completed_{pk}'
        if field_name in request.POST:
            obj.is_completed = request.POST.get(field_name) == "on"
        else:
            obj.is_completed = False
        obj.save()
        return redirect(self.success_url)

class TodoUpdateView(generic.UpdateView):
    model = TodoItems
    form_class = TodoUpdateModelForm
    template_name = 'todo/todo-update.html'
    success_url = reverse_lazy('todo-main')

class TodoDeleteView(generic.DeleteView):
    model = TodoItems
    success_url = reverse_lazy('todo-main')
    http_method_names = ['post']
