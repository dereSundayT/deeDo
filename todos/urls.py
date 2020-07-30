from django.urls import path
from .views import AddNewTodo, TodoListView,TodoDetail, AddNewLabel, LabelLists, LabelDetail

urlpatterns = [
    # todo
    path('', TodoListView.as_view(), name='todos-list'),
    path('todo/new', AddNewTodo.as_view(), name='todos-add'),
    path('todo/<int:pk>',TodoDetail.as_view(),name="todos-detail"),
    # lablel
    path('label/new/', AddNewLabel.as_view(), name="todos-create-label"),
    path('label/<int:pk>/', LabelDetail.as_view(), name="todos-label-detail"),

]
