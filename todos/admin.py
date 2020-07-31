from django.contrib import admin
from .models import Label, Todo, TodoLevel
# Register your models here.

admin.site.register(Label)
admin.site.register(Todo)
admin.site.register(TodoLevel)
