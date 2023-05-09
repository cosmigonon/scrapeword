from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class RegisterPageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)


class ProfileSettingsPageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/settings/profile/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("accounts-settings"))
        self.assertEqual(response.status_code, 200)
