from django import forms
from .models import UserGlossary


LAN_CODES = [
    ("de", "German"),
    ("el", "Greek"),
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("pt", "Portuguese"),
    ("ru", "Russian"),
    ("zh", "Chinese"),
]


class SourceLanForm(forms.ModelForm):
    source_language = forms.CharField(
        label="source language", widget=forms.Select(choices=LAN_CODES), max_length=5
    )

    class Meta:
        model = UserGlossary
        fields = "source_language"


class TargetLanForm(forms.ModelForm):
    target_language = forms.CharField(
        label="target language", widget=forms.Select(choices=LAN_CODES), max_length=5
    )

    class Meta:
        model = UserGlossary
        fields = "target_language"
