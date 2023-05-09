from django.test import TestCase
from django.urls import reverse


class IndexPageTests(TestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)


class DashboardPageTests(TestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("dashboard-home"))
        self.assertEqual(response.status_code, 200)


class CreatePageTests(TestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("create"))
        self.assertEqual(response.status_code, 200)


class SettingsPageTests(TestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/settings/general/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("general-settings"))
        self.assertEqual(response.status_code, 200)
