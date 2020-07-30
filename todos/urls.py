from django.urls import path
from .views import (testView, isCompleted, AddNewTodo, TodoListView, TodoDetail, AddNewLabel, LabelLists, LabelDetail,
                    TodoUpdateView, TodoDeleteView, LabelLists, LabelUpdateView,LabelDeleteView)

urlpatterns = [
    #
    path('test', testView, name='test'),
    path('', TodoListView.as_view(), name='todos-list'),
    path('todo/new', AddNewTodo.as_view(), name='todos-add'),
    path('todo/<int:pk>', TodoDetail.as_view(), name="todos-detail"),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name="todos-update"),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name="todos-delete"),
    path('todo/<int:pk>/<int:state>/completed/',isCompleted, name="todos-is-completed"),
    # lablel
    path('label/', LabelLists.as_view(), name="todos-label-list"),
    path('label/new/', AddNewLabel.as_view(), name="todos-label-create"),
    path('label/<int:pk>/', LabelDetail.as_view(), name="todos-label-detail"),
    path('label/<int:pk>/update/', LabelUpdateView.as_view(),name="todos-label-update"),
    path('label/<int:pk>/delete/', LabelDeleteView.as_view(),name="todos-label-delete"),

]
"""
A user should be able to set priority for each TODO

Arrange each TODO by their priority. (Use order_by in Django models)

Identify each user using authentication and authorization: 
"""