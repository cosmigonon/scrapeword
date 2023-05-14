from django.test import TestCase
from dashboard.models import (
    UserDeck,
    GlossaryWord,
    GlossarySentence,
    TransWord,
    TransSentence,
)


class UserDeckTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = UserDeck.objects.create(deck_name="My portuguese vocabulary")
        cls.template = UserDeck.objects.create(deck_template=" ")
        cls.user = UserDeck.objects.create(user_id="Hermeto")

    def test_model_content_deck_name(self):
        self.assertEqual(self.name.deck_name, "My portuguese vocabulary")

    def test_model_content_deck_template(self):
        self.assertEqual(self.template.deck_template, " ")

    def test_model_content_user_id(self):
        self.assertEqual(self.user.user_id, "Hermeto")
