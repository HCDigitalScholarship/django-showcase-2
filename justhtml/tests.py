from django.test import TestCase


class JustHTMLTests(TestCase):
    def test_home_page_uses_right_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "justhtml/index.html")
