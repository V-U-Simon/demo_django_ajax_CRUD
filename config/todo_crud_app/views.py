from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseBadRequest, JsonResponse

from .models import Task


class TaskView(generic.TemplateView):
    template_name = 'todo_crud_app/task_ajax.html'


class AjaxTaskView(generic.View):

    def get(self, request):
        if request.accepts('application/json'):
            tasks = list(Task.objects.all().values('title', 'complited'))
            return JsonResponse({'context': tasks})

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delte(self, request):
        pass