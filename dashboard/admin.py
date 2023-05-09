from django.contrib import admin
from django.apps import apps
from .models import *


dashboard_models = apps.get_app_config("dashboard").get_models()

for model in dashboard_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
