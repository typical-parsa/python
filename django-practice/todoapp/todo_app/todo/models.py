from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description =models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
     