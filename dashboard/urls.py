from django.urls import path
from .views import IndexView, DashboardListView, create, AppSettingsView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dashboard/", DashboardListView.as_view(), name="dashboard-home"),
    path("create/", create, name="create"),
    path("settings/general/", AppSettingsView.as_view(), name="general-settings"),
]
