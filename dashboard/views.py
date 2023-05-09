from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from accounts.models import CustomUser
from .models import GlossaryWord, GlossarySentence, TransWord, TransSentence, UserDeck


def index(request):
    return render(request, "index.html")


class DashboardView(ListView):
    model = GlossaryWord
    context_object_name = "words_list"
    template_name = "dashboard/base_dashboard.html"


def create(request):
    return render(request, "dashboard/base_create.html")


class AppSettingsView(TemplateView):
    template_name = "dashboard/base_settings.html"
