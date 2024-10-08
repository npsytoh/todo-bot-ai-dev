import datetime as dt

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import TodoItems
from .forms import TodoCreateModelForm
from .forms import TodoEditModelForm


class TodoMainView(generic.ListView, generic.edit.ModelFormMixin):
    model = TodoItems
    form_class = TodoCreateModelForm
    template_name = 'todo/todo-main.html'
    context_object_name = 'todo_list'
    success_url = reverse_lazy('todo-main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_item"] = TodoEditModelForm(self.request.POST or None)
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(status=False).order_by('-updated_at')
        for data in queryset:
            if data.due_date is None:
                data.due_date = '-'
        return queryset

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


class TodoItemPostView(generic.FormView):
    model = TodoItems
    success_url = reverse_lazy('todo-main')
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        task_id = self.kwargs.get('task_id')
        obj = get_object_or_404(self.model, task_id=task_id)
        target_field = self.kwargs.get('target_field')
        self.update_state(request,obj,target_field)
        return redirect(self.success_url)
    
    def update_state(self,request,obj,field_name):
        is_enable = request.POST.get('itemState') == 'true'
        if field_name == 'status':
            obj.status = is_enable
            if is_enable:
                obj.completed_at = dt.datetime.now()
            else:
                obj.completed_at = None
        elif field_name == 'important':
            obj.is_important = is_enable
        obj.save()


class TodoEditView(generic.UpdateView):
    model = TodoItems
    form_class = TodoEditModelForm
    template_name = 'todo/todo-edit.html'
    slug_field = 'task_id'
    slug_url_kwarg = 'task_id'
    success_url = reverse_lazy('todo-main')


class TodoDeleteView(generic.DeleteView):
    model = TodoItems
    slug_field = 'task_id'
    slug_url_kwarg = 'task_id'
    success_url = reverse_lazy('todo-main')
    http_method_names = ['post']
