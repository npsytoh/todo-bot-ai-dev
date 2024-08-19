from django.urls import reverse_lazy
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

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     print(form.instance.pk)
    #     return response

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

class TodoCheckToggleView(generic.UpdateView):
    model = TodoItems
    fields = ['is_completed']
    success_url = reverse_lazy('todo-main')
    http_method_names = ['post']

    def form_valid(self, form):
        print(self.request.POST)
        post = form.save(commit=False)
        post.is_completed = True
        post.save()
        return super().form_valid(form)

class TodoUpdateView(generic.UpdateView):
    model = TodoItems
    form_class = TodoUpdateModelForm
    template_name = 'todo/todo-update.html'
    success_url = reverse_lazy('todo-main')

class TodoDeleteView(generic.DeleteView):
    model = TodoItems
    success_url = reverse_lazy('todo-main')
    http_method_names = ['post']
