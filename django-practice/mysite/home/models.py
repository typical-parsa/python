from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name