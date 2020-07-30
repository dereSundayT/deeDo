from django.shortcuts import render, redirect
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

# def loginView(request):
#     if request.METHOD == 'POST':

#     return render(request, 'accounts/login.html',{'form':form})
