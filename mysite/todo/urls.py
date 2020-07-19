from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task-delete/<int:pk>', views.task_delete, name='task_delete'),
    path('task-update/<int:pk>', views.task_update, name='task_update'),
    path('task-completed/<int:pk>', views.task_completed, name='task_completed'),
]
