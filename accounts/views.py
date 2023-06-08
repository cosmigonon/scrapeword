from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("dashboard_home")
    template_name = "registration/signup.html"


class ProfileSettingsView(TemplateView):
    template_name = "accounts/base_profile.html"
