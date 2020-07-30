from django.urls import path
from .views import home, AddNewLabel, LabelLists, LabelDetail

urlpatterns = [
    path('', home, name='todos-home'),
    path('label/new/', AddNewLabel.as_view(), name="todos-create-label"),
    path('label/<int:pk>/', LabelDetail.as_view(), name="todos-label-detail"),

]
