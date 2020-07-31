from django.urls import path
from .views import register,Login,Logout,profileView


urlpatterns = [
    path('register/',register,name="account-register"),
    path('login/', Login.as_view(),name="account-login"),
    path('logout/',Logout.as_view(),name="account-logout"),
    path('profile/',profileView,name="account-profile"),
]
