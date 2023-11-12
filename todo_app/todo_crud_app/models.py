from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
