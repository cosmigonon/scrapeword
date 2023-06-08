from django.test import TestCase
from django.contrib.auth import get_user_model
from dashboard.models import UserDeck, UserGlossary


class UserDeckTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="testuser", email="test@email.com", password="supersecret_password"
        )
        cls.deck = UserDeck.objects.create(
            deck_name="deck_test", deck_template="", user=cls.user
        )


class UserGlossaryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.vocab = UserGlossary.objects.create(
            vocabulary="test sentence", source_language="en", target_language="pt"
        user=cls.user)
