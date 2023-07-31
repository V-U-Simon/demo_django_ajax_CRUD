from django.shortcuts import render
from django.views import generic

from .models import Task


class TaskView(generic.TemplateView):
    template_name = 'todo_crud_app/task_ajax.html'
