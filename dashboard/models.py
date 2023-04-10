from django.db import models
from django.conf import settings
from accounts.models import CustomUser
from core.constants import LANGUAGE_CODES as LAN_CODES

#lan_codes = [(k, k.capitalize()) for k, v in LAN_CODES.items()] # List of tuples from the language codes dictionary.



class Translator(models.Model):

    class WebTranslators(models.TextChoices):
        GOOGLE = 'goo_trans', 'Google Translate'
        DEEPL = 'deepl_trans', 'DeepL Translator'
        CAMBRIDGE = 'cambridge_dict', 'Cambridge Dictionary'
        LAROUSSE = 'larousse_dict', 'Larousse Dictionary'

    class Meta:
        db_table = 'translate_services'
    
    translator = models.CharField(
        max_length= 20, 
        choices=WebTranslators.choices
        )

    def __str__(self):
        return self.translator


class Language(models.Model):

    class LanCode(models.TextChoices):
        GERMAN = 'de', 'German'
        GREEK = 'el', 'Greek'
        ENGLISH = 'en', 'English'
        SPANISH = 'es', 'Spanish'
        FRENCH = 'fr', 'French'
        ITALIAN = 'it', 'Italian'
        JAPANESE = 'ja', 'Japanese'
        PORTUGUESE = 'pt', 'Portuguese'
        RUSSIAN = 'ru', 'Russian'
        CHINESE = 'zh', 'Chinese'

    language_code = models.CharField(
        max_length=15, 
        choices=LanCode.choices
        )
    
    class Meta:
        db_table = 'language'
    
    def __str__(self):
        return f'code: {self.language_code}'
    

class GlossaryWord(models.Model):
    word = models.TextField(unique=True)
    user_glossary_word = models.ManyToManyField(CustomUser) # Linking table with user_id and word_id foreign keys.
    source_language = models.OneToOneField(Language, on_delete=models.CASCADE)
    grammatical_category = models.TextField()
    tag = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    class Meta:
        db_table = 'glossary_word'

    def __str__(self):
        return self.word


class GlossarySentence(models.Model):
    sentence = models.TextField(unique=True)
    user_glossary_sentence = models.ManyToManyField(CustomUser) # Linking table with user_id and sentence_id foreign keys.
    source_language = models.OneToOneField(Language, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    class Meta:
        db_table = 'expressions_vocabulary'

    def __str__(self):
        return self.sentence
    

class TransWord(models.Model):
    translated_word = models.TextField(blank=True)
    target_language = models.OneToOneField(Language, on_delete=models.CASCADE) 
    word = models.ForeignKey(GlossaryWord, on_delete=models.CASCADE)
    class Meta:
        db_table = 'translated_glossary_word'

    def __str__(self):
        return self.translated_word


class TransSentence(models.Model):
    translated_sentence = models.TextField(blank=True)
    target_language = models.OneToOneField(Language, on_delete=models.CASCADE) 
    sentence = models.OneToOneField(GlossarySentence, on_delete=models.CASCADE)
    class Meta:
        db_table = 'translated_glossary_sentence'

    def __str__(self):
        return self.translated_sentence

