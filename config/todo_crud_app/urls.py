from django.urls import path
from .apps import TodoCrudAppConfig
from . import views

app_name = TodoCrudAppConfig.name

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
]
