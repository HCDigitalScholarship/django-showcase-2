from django.test import TestCase


class TableBuilderTests(TestCase):
    def test_index_page_uses_right_template(self):
        response = self.client.get("/tablebuilder/")
        self.assertTemplateUsed(response, "tablebuilder/index.html")
