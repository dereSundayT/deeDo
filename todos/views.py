from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView
from .models import Label, Todo

# Create your views here.


def home(request):
    context = {
        'title': 'My deeDo Lists',
        'todos': Todo.objects.filter(status=True),
    }
    return render(request, 'index.html', context)

# class HomeListView(ListView):
    model: Todo


class AddNewLabel(CreateView):
    model = Label
    fields = ['title']


class LabelLists(ListView):
    model = Label

class LabelDetail(DetailView):
    model = Label


