from django.db import models
from django.conf import settings
from django.urls import reverse


class UserDeck(models.Model):
    deck_name = models.CharField(verbose_name="deck name", max_length=100)
    deck_template = models.TextField(verbose_name="template", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_deck"
        verbose_name = "deck"
        verbose_name_plural = "decks"

    def __str__(self):
        return self.deck_name

    def get_absolute_url(self):
        return reverse("deck_detail", kwargs={"pk": self.pk})


class UserGlossary(models.Model):
    vocabulary = models.CharField(max_length=5000)
    source_language = models.CharField(max_length=50)
    grammatical_category = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deck = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, blank=True, null=True)
    word = models.BooleanField(blank=True)
    sentence = models.BooleanField(blank=True)
    date = models.DateField(verbose_name="date added", auto_now=True)

    class Meta:
        db_table = "user_glossary"
        verbose_name = "vocabulary"
        verbose_name_plural = "vocabularies"

    def __str__(self):
        return self.vocabulary

    def get_absolute_url(self):
        return reverse("glossary_detail", kwargs={"pk": self.pk})


class TransGlossary(models.Model):
    translation = models.TextField(blank=True, null=True)
    target_language = models.CharField(max_length=50)
    vocabulary = models.ForeignKey(UserGlossary, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deck = models.ForeignKey(UserDeck, on_delete=models.CASCADE)

    class Meta:
        db_table = "glossary_translations"
        verbose_name = "translation"
        verbose_name_plural = "translations"

    def __str__(self):
        return self.translation

    def get_absolute_url(self):
        return reverse("glossary_translations_detail", kwargs={"pk": self.pk})
