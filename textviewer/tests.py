"""
Unit tests for the textviewer app.

See justhtml/tests.py for an explanation of Django unit tests
"""
from django.test import TestCase


class TextViewerTests(TestCase):
    def test_index_page_uses_right_template(self):
        response = self.client.get("/texts/")
        self.assertTemplateUsed(response, "textviewer/index.html")
