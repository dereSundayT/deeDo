from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Label, Todo

# Create your views here.


def testView(request):
    return render(request, 'test.html')

# CreateView
class AddNewTodo(LoginRequiredMixin,CreateView):
    model = Todo
    #label = Label.objects.filter(owner=request.user)
    fields = ['title', 'label', 'description']


    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# #ListView
class TodoListView(LoginRequiredMixin,ListView):
    model = Todo
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


# DetailView
class TodoDetail(LoginRequiredMixin,DetailView):
    model = Todo

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    

# UpdateView


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'label', 'description']

# DeleteView


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos-list')

# CompletedView

@login_required
def isCompleted(request, pk, state):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user == todo.owner:
        if state == 0:
            # status will be equal to False
            todo.status = False
            todo.save()
        else:
            # status will be equal to True
            todo.status = True
            todo.save()
    else:
        return render(request,'todos/todos_list.html')

    return redirect('todos-detail', pk=pk)

# CreateView
class AddNewLabel(LoginRequiredMixin,CreateView):
    model = Label
    fields = ['title']

    def form_valid(self, form):
        # setting the author of label
        form.instance.owner = self.request.user
        return super().form_valid(form)

# #ListView
class LabelLists(ListView):
    model = Label

    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)

# #DetailView
class LabelDetail(LoginRequiredMixin,DetailView):
    model = Label

    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)

# #UpdateView
class LabelUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Label
    fields = ['title']

    def test_func(self):
        label = self.get_object()
        if label.owner == self.request.user:
            return True
        return False

# #DeleteView
class LabelDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Label
    success_url = reverse_lazy('todos-label-list')

    def test_func(self):
        label = self.get_object()

        if label.owner == self.request.user:
            return True 
        return False


