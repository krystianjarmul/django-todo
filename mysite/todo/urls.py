from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task_delete/<int:pk>', views.task_delete, name='task_delete'),
    path('task_completed/<int:pk>', views.task_completed, name='task_completed'),
]
