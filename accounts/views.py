from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('todos-list')

    else:
        form = UserRegisterForm()

    return render(request, 'accounts/reg.html', {'form': form})


class Login(LoginView):
    template_name = "accounts/login.html"

class Logout(LogoutView):
    template_name = "accounts/logout.html"

@login_required
def profileView(request):
    return render(request, 'accounts/profile.html')
