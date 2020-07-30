from django.db import models

# Create your models here.
class Label(models.Model):
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=1)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    label = models.ForeignKey(Label,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)



