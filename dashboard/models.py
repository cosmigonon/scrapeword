from django.db import models
from django.conf import settings
from django.urls import reverse


class UserDeck(models.Model):
    deck_name = models.CharField(verbose_name="deck name", max_length=100)
    deck_template = models.TextField(verbose_name="template", blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        db_table = "user_deck"
        verbose_name = "deck"
        verbose_name_plural = "decks"

    def __str__(self):
        return self.deck_name

    def get_absolute_url(self):
        return reverse("deck_detail", kwargs={"slug": self.slug})


class UserGlossary(models.Model):
    GERMAN = "de"
    GREEK = "el"
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    ITALIAN = "it"
    JAPANESE = "ja"
    PORTUGUESE = "pt"
    RUSSIAN = "ru"
    CHINESE = "zh"
    LANGUAGE_CHOICES = [
        (GERMAN, "German"),
        (GREEK, "Greek"),
        (ENGLISH, "English"),
        (SPANISH, "Spanish"),
        (FRENCH, "French"),
        (ITALIAN, "Italian"),
        (JAPANESE, "Japanese"),
        (PORTUGUESE, "Portuguese"),
        (RUSSIAN, "Russian"),
        (CHINESE, "Chinese"),
    ]

    WORD = "w"
    SENTENCE = "s"
    CATEGORY_CHOICES = [
        (WORD, "word"),
        (SENTENCE, "sentence"),
    ]

    vocabulary = models.CharField(max_length=5000)
    source_language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    translation = models.TextField(blank=True, null=True)
    target_language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    grammatical_category = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deck = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, blank=True)
    date = models.DateField(verbose_name="date added", auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        db_table = "user_glossary"
        verbose_name = "vocabulary"
        verbose_name_plural = "vocabularies"

    def __str__(self):
        return self.vocabulary

    def get_absolute_url(self):
        return reverse("glossary_detail", kwargs={"slug": self.slug})
