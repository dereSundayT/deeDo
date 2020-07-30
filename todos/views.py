from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Label, Todo

# Create your views here.


def testView(request):
    return render(request, 'test.html')

# CreateView


class AddNewTodo(CreateView):
    model = Todo
    fields = ['title', 'label', 'description']

# #ListView


class TodoListView(ListView):
    model = Todo

# DetailView


class TodoDetail(DetailView):
    model = Todo

# UpdateView


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'label', 'description']

# DeleteView


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos-list')

# CompletedView


def isCompleted(request, pk, state):
    todo = get_object_or_404(Todo, pk=pk)
    if state == 0:
        # status will be equal to False
        todo.status = False
        todo.save()
    else:
        # status will be equal to True
        todo.status = True
        todo.save()
    return redirect('todos-detail', pk=pk)

# CreateView
class AddNewLabel(CreateView):
    model = Label
    fields = ['title']
# #ListView
class LabelLists(ListView):
    model = Label
# #DetailView
class LabelDetail(DetailView):
    model = Label
# #UpdateView
class LabelUpdateView(UpdateView):
    model = Label
    fields = ['title']
# #DeleteView
class LabelDeleteView(DeleteView):
    model = Label
    success_url = reverse_lazy('todos-label-list')

# #D
