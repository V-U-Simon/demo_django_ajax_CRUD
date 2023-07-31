from django.urls import path
from .apps import TodoCrudAppConfig
from . import views

app_name = TodoCrudAppConfig.name

urlpatterns = [
    path('', views.TaskView.as_view(), name='home'),
    path('task/', views.AjaxTaskView.as_view(), name='tasks'),
    path('task/<int:id>', views.AjaxTaskView.as_view(), name='task'),
]
