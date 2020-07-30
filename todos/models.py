from django.db import models
from django.urls import reverse

# Create your models here.


class Label(models.Model):
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=1)

    def get_absolute_url(self):
        return reverse("todos-label-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("todos-detail", kwargs={"pk": self.pk})
