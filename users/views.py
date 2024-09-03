from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            form.save()
            return redirect('blog-home')
    else:
        form = RegisterForm()
    form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

