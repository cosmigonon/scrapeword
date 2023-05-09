from django.urls import path
from . import views
from .views import ProfileSettingsView


urlpatterns = [
    path("signup/", views.register, name="signup"),
    path("settings/profile/", ProfileSettingsView.as_view(), name="accounts-settings"),
]
