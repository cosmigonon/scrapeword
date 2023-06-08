from django.urls import path
from .views import SignUpView, ProfileSettingsView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("settings/profile/", ProfileSettingsView.as_view(), name="accounts_settings"),
]
