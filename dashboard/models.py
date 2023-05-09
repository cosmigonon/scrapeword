from django.db import models
from django.conf import settings
from accounts.models import CustomUser


class UserDeck(models.Model):
    deck_name = models.CharField(max_length=100)
    deck_template = models.TextField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_deck"

    def __str__(self):
        return self.deck_name


class GlossaryWord(models.Model):
    word = models.CharField(max_length=100)
    source_language = models.CharField(max_length=2)
    grammatical_category = models.CharField(max_length=50, null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    deck_id = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, null=True)
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = "glossary_word"

    def __str__(self):
        return self.word


class GlossarySentence(models.Model):
    sentence = models.CharField(max_length=5000)
    source_language = models.CharField(max_length=5)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    deck_id = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, null=True)
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = "glossary_sentence"

    def __str__(self):
        return self.sentence


class TransWord(models.Model):
    translated_word = models.CharField(max_length=500, blank=True)
    target_language = models.CharField(max_length=2)
    word_id = models.ForeignKey(GlossaryWord, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=5)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "translated_glossary_word"

    def __str__(self):
        return self.translated_word


class TransSentence(models.Model):
    translated_sentence = models.TextField(blank=True)
    target_language = models.CharField(max_length=5)
    sentence_id = models.OneToOneField(GlossarySentence, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=5)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "translated_glossary_sentence"

    def __str__(self):
        return self.translated_sentence
