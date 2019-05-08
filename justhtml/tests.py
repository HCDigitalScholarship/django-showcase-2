from django.test import TestCase


class JustHTMLTests(TestCase):
    def test_index_page_uses_right_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "justhtml/index.html")

    def test_failure(self):
        self.assertTrue(False)
