"""
Unit tests for the interns app.

These tests make sure that visiting each URL that the app defines results in the
expected template being returned. Unlike the functional tests in the top-level tests/
directory, it does not test the appearance or behavior of the web page as the browser
would actually render it.
"""
from django.test import TestCase


class InternsTest(TestCase):
    def test_index_page(self):
        response = self.client.get("/interns/")
        self.assertTemplateUsed(response, "interns/index.html")

    def test_iafisher_page(self):
        response = self.client.get("/interns/iafisher")
        self.assertTemplateUsed(response, "interns/iafisher.html")

    def test_yayad_page(self):
        response = self.client.get("/interns/yayad")
        self.assertTemplateUsed(response, "interns/yayad.html")

    def test_mzarafon_page(self):
        response = self.client.get("/interns/mzarafon")
        self.assertTemplateUsed(response, "interns/mzarafon.html")
