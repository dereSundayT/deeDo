from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Label, Todo

# Create your views here.

#CreateView 
class AddNewTodo(CreateView):
    model=Todo
    fields = ['title','label','description']
# #ListView 
class TodoListView(ListView):
    model = Todo
#DetailView
class TodoDetail(DetailView):
    model = Todo
#UpdateView


##DeleteView

#CompletedView









class AddNewLabel(CreateView):
    model = Label
    fields = ['title']

class LabelLists(ListView):
    model = Label

class LabelDetail(DetailView):
    model = Label
