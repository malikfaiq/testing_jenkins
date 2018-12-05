from django.test import TestCase
from django.urls import reverse


class StartAppTests(TestCase):

    def test_start_app__correct_response(self):
        response = self.client.get(reverse("start_app"))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, b"hello_jenkins")

    def test_start_app_wrong_response(self):
        response = self.client.get(reverse("start_app"))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, b"hello_jen")
