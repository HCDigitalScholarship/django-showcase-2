"""
Unit tests for the justhtml app.

These tests make sure that visiting each URL that the app defines results in the
expected template being returned. Unlike the functional tests in the top-level tests/
directory, it does not test the appearance or behavior of the web page as the browser
would actually render it.
"""
from django.test import TestCase


class JustHTMLTests(TestCase):
    """
    Test cases are grouped together into classes. Usually we just have one class per
    tests.py file, but if you ever have a large number of tests with a more logical way
    to group them, then you might consider having multiple test classes.
    """

    def test_index_page_uses_right_template(self):
        """
        Each method of this class that begins with test_ defines a test case.

        Test cases should only test one thing when possible.
        """
        response = self.client.get("/")
        self.assertTemplateUsed(response, "justhtml/index.html")
