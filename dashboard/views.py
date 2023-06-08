from typing import Any, Dict
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from accounts.models import CustomUser
from .models import UserDeck, UserGlossary


class HomeView(TemplateView):
    template_name = "index.html"


class GuideView(TemplateView):
    template_name = "dashboard/base_guide.html"


class DashboardListView(ListView):
    model = UserDeck
    context_object_name = "deck"
    template_name = "dashboard/base_dashboard.html"

    def get_queryset(self):
        user = self.request.user
        account = CustomUser.objects.get(id=user.id)
        return UserDeck.objects.filter(user=account)


class GlossaryListView(ListView):
    model = UserGlossary
    context_object_name = "glossary"
    template_name = "dashboard/base_glossary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = UserDeck.objects.filter(user=user_id)
        return context


class GlossaryDetailView(DetailView):
    model = UserGlossary
    context_object_name = "vocab"
    template_name = "dashboard/base_detail_flashcard.html"


class GlossaryCrateView(CreateView):
    model = UserGlossary
    template_name = "dashboard/base_create_flashcard.html"
    fields = [
        "vocabulary",
        "source_language",
        "translation",
        "target_language",
        "grammatical_category",
        "deck",
        "tag",
        "category",
    ]


class AppSettingsView(TemplateView):
    template_name = "dashboard/base_settings.html"
