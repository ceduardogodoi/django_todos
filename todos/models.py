from os import name
from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    is_completed = models.BooleanField()

    def __str__(self):
        return self.task
