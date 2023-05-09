from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard/base_dashboard.html")


def create(request):
    return render(request, "dashboard/base_create.html")


class AppSettingsView(TemplateView):
    template_name = "dashboard/base_settings.html"
