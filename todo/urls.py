from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoMainView.as_view(), name='todo-main'),
]
