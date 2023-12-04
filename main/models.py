from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    completion = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
