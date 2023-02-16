from django.db import models

class Task(models.Model):
    body = models.TextField()                       # Task that needs to be done
    completed = models.BooleanField(default=False)  # Status of the task is by default set as "Not done"
