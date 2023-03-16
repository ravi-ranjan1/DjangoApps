from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse


def dashboard(request):
    return render(request, 'user_management/dashboard.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


# def registration(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return redirect(reverse('dashboard'))
#         return render(request, 'registration/register.html' , {'form':form})