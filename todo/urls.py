from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoMainView.as_view(), name='todo-main'),
    path('items/<int:pk>/check-toggle/', views.TodoCheckToggleView.as_view(), name='todo-check-toggle'),
    path('items/<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo-update'),
    path('items/<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo-delete'),
]
