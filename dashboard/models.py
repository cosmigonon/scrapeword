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


class GlossaryWord(models.Model):
    word = models.CharField(max_length=100)
    source_language = models.CharField(max_length=2)
    grammatical_category = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deck = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(verbose_name="date added", auto_now=True)

    class Meta:
        db_table = "word_glossary"
        verbose_name = "word"
        verbose_name_plural = "words"

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse("glossary_word_detail", kwargs={"pk": self.pk})


class GlossarySentence(models.Model):
    sentence = models.CharField(max_length=5000)
    source_language = models.CharField(max_length=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deck = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(verbose_name="date added", auto_now=True)

    class Meta:
        db_table = "sentence_glossary"
        verbose_name = "sentence"
        verbose_name_plural = "sentences"

    def __str__(self):
        return self.sentence

    def get_absolute_url(self):
        return reverse("glossary_sentence_detail", kwargs={"pk": self.pk})


class TransWord(models.Model):
    word_translation = models.CharField(max_length=500, blank=True)
    target_language = models.CharField(max_length=2)
    word = models.ForeignKey(GlossaryWord, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "word_translations_glossary"
        verbose_name = "word translation"
        verbose_name_plural = "words translations"

    def __str__(self):
        return self.word_translation

    def get_absolute_url(self):
        return reverse("word_translation_detail", kwargs={"pk": self.pk})


class TransSentence(models.Model):
    sentence_translation = models.TextField(blank=True)
    target_language = models.CharField(max_length=5)
    sentence = models.OneToOneField(GlossarySentence, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "sentence_translations_glossary"
        verbose_name = "sentence translation"
        verbose_name_plural = "sentences translations"

    def __str__(self):
        return self.sentence_translation

    def get_absolute_url(self):
        return reverse("sentence_translation_detail", kwargs={"pk": self.pk})
