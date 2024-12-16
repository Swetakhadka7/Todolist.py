from django.db import models

# Create your models here.
#Fields
#title, description, status
class Todolist(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status =models.BooleanField(default=False)

