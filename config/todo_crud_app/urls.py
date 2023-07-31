from django.urls import path
from .apps import TodoCrudAppConfig
from . import views

app_name = TodoCrudAppConfig.name

urlpatterns = [
    path('', views.TaskView.as_view(), name='ajax_crud'),
]
