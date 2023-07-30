from django.urls import path
from .apps import TodoCrudAppConfig

app_name = TodoCrudAppConfig.name

urlpatterns = [
    # path('', include('todo_crud_app.urls'), namespace='crud'),
]
