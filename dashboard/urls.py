from django.urls import path
from .views import (
    HomeView,
    GuideView,
    DashboardListView,
    GlossaryCrateView,
    AppSettingsView,
    GlossaryListView,
    GlossaryDetailView,
)


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("learn/", GuideView.as_view(), name="guide"),
    path("dashboard/", DashboardListView.as_view(), name="dashboard_home"),
    path("create/", GlossaryCrateView.as_view(), name="create"),
    path("settings/general/", AppSettingsView.as_view(), name="general_settings"),
    path("glossary/<slug:slug>", GlossaryListView.as_view(), name="deck_detail"),
    path("<slug:slug>/", GlossaryDetailView.as_view(), name="glossary_detail"),
]
