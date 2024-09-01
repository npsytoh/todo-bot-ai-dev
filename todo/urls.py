from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoMainView.as_view(), name='todo-main'),
    path('items/<int:pk>/check-toggle/', views.TodoCheckToggleView.as_view(), name='todo-check-toggle'),
    path('items/edit/<slug:task_id>/', views.TodoEditView.as_view(), name='todo-edit'),
    path('items/delete/<slug:task_id>/', views.TodoDeleteView.as_view(), name='todo-delete'),
]
