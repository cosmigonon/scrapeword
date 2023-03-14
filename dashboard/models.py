from django.db import models
from django.contrib.auth.models import User 





class Language(models.Model):
    language_name = models.CharField(max_length=20)
    language_code = models.CharField(max_length=5, primary_key=True)

    class Meta:
        db_table = 'language'


class WordVocabulary(models.Model):
    word = models.TextField()
    languague_code = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        db_table = 'word_vocabulary'
    

class ExpressionsVocabulary(models.Model):
    sentence = models.TextField()

    class Meta:
        db_table = 'expressions_vocabulary'


class TranslatedWords(models.Model):
    
    
    class Meta:
        db_table = 'translated_words'

class TranslatedExpressions(models.Model):

    class Meta:
        db_table = 'translated_expressions'

