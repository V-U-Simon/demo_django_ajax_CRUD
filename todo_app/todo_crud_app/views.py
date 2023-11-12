import json
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Task


class TaskView(generic.TemplateView):
    template_name = 'todo_crud_app/task_ajax.html'


class AjaxTaskView(generic.View):

    def get(self, request):
        if not request.accepts('application/json'):
            return JsonResponse({'error': 'wrong content type'})
        tasks = list(Task.objects.all().values('id', 'title', 'completed'))
        return JsonResponse({'context': tasks})

    def post(self, request):
        if not request.accepts('application/json'):
            return JsonResponse({'error': 'wrong content type'})
        task = json.loads(request.body)
        task = Task.objects.create(title=task['title'], completed=bool(task['completed']))
        return JsonResponse({'status': f'task is created: {task.title} (id: {task.id})'})

    def put(self, request):
        if not request.accepts('application/json'):
            return JsonResponse({'error': 'wrong content type'})
        updated_task = json.loads(request.body)

        task = get_object_or_404(Task, id=int(updated_task['taskId']))
        task.title = updated_task['title']
        task.completed = bool(updated_task['completed'])
        task.save()
        return JsonResponse({'status': f'task is updated: {task.title}, {task.completed} (id: {task.id})'})

    def delete(self, request):
        if not request.accepts('application/json'):
            return JsonResponse({'error': 'wrong content type'})
        task_id = json.loads(request.body).get('taskId')
        Task.objects.get(id=task_id).delete()
        return JsonResponse({'status': f'task is deteted (id: {task_id})'})