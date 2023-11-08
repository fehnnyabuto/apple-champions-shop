from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages


def register(request):
    # if form is valid return empty form
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully')
            return redirect('register-url')
    else:
        form = RegistrationForm()

    return render(request, 'auth/register.html', {"form": form})
