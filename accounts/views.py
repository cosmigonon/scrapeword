from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import TemplateView


def register(request):
    if request == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, "Your account was successfully created")
            return redirect("dashboard-home")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


class ProfileSettingsView(TemplateView):
    template_name = "accounts/base_profile.html"
