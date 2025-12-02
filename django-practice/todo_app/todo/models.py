from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    author = models.IntegerField()
    title = models.CharField()
    description = models.TextField()
    category = models.CharField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'