from django.urls import path
from .views import index, DashboardView, create, AppSettingsView


urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", DashboardView.as_view(), name="dashboard-home"),
    path("create/", create, name="create"),
    path("settings/general/", AppSettingsView.as_view(), name="general-settings"),
]
