from django.db import models
from django.contrib.auth.models import User 


class Language(models.Model):
    language_name = models.CharField(max_length=20)
    language_code = models.CharField(max_length=5)
    class Meta:
        db_table = 'language'


class GlossaryWord(models.Model):
    word = models.TextField()
    languague = models.OneToOneField(Language, on_delete=models.CASCADE)
    grammatical_category = models.TextField() 
    class Meta:
        db_table = 'glossary_word'


class UserGlossaryWord(models.Model):
    word = models.ManyToManyField(User, GlossaryWord)
    class Meta:
        db_table = 'user_glossary_word' 


class GlossarySentence(models.Model):
    sentence = models.TextField()
    languague = models.OneToOneField(Language, on_delete=models.CASCADE)
    class Meta:
        db_table = 'expressions_vocabulary'


class UserGlossarySentence(models.Model):
    sentence = models.ManyToManyField(User,GlossarySentence)
    class Meta:
        db_table = 'user_glossary_sentence'


class TransWord(models.Model):
    translated_word = models.TextField()
    language = models.OneToOneField(Language, on_delete=models.CASCADE) 
    word = models.ForeignKey(GlossaryWord, on_delete=models.CASCADE)
    class Meta:
        db_table = 'translated_glossary_word'


class TransSentence(models.Model):
    translated_sentence = models.TextField()
    language = models.OneToOneField(Language, on_delete=models.CASCADE) 
    sentence = models.OneToOneField(GlossarySentence, on_delete=models.CASCADE)
    class Meta:
        db_table = 'translated_glossary_sentence'

