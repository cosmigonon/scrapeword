from django.urls import path
from . import views
from .views import AppSettingsView


urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard-home"),
    path("create/", views.create, name="create"),
    path("settings/general/", AppSettingsView.as_view(), name="general-settings"),
]
