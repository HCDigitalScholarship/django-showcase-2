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
        self.arrestTemplateUsed(response, "interns/yayad.html")
