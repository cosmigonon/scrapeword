from django.contrib import admin
from django.apps import apps
from .models import UserDeck, UserGlossary


class DeckAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": (
            "user",
            "deck_name",
        )
    }


class GlossaryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("vocabulary",)}


admin.site.register(UserDeck, DeckAdmin)
admin.site.register(UserGlossary, GlossaryAdmin)
