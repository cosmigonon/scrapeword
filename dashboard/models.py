from django.db import models
from django.conf import settings


class UserDeck(models.Model):
    deck_name = models.CharField(verbose_name="deck", max_length=100)
    deck_template = models.TextField(verbose_name="template", blank=True, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_deck"

    def __str__(self):
        return self.deck_name


class GlossaryWord(models.Model):
    word = models.CharField(max_length=100)
    source_language = models.CharField(max_length=2)
    grammatical_category = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deck_id = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(verbose_name="date added", auto_now=True)

    class Meta:
        db_table = "word_glossary"

    def __str__(self):
        return self.word


class GlossarySentence(models.Model):
    sentence = models.CharField(max_length=5000)
    source_language = models.CharField(max_length=5)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deck_id = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(verbose_name="date added", auto_now=True)

    class Meta:
        db_table = "sentence_glossary"

    def __str__(self):
        return self.sentence


class TransWord(models.Model):
    word_translation = models.CharField(max_length=500, blank=True)
    target_language = models.CharField(max_length=2)
    word_id = models.ForeignKey(GlossaryWord, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=5)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "word_translations_glossary"

    def __str__(self):
        return self.word_translation


class TransSentence(models.Model):
    sentence_translation = models.TextField(blank=True)
    target_language = models.CharField(max_length=5)
    sentence_id = models.OneToOneField(GlossarySentence, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=5)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "sentence_translations_glossary"

    def __str__(self):
        return self.sentence_translation
