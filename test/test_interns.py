"""
Functional tests for the interns app.

Strictly speaking we don't need a functional test for static HTML -- we could just test
it with the Django test runner and avoid the overhead of using Selenium. The point of
this test suite is rather so that new interns can get practice writing functional tests.
"""


def test_can_visit_iafisher_page(url, browser):
    browser.get(url + "/interns/iafisher")

    assert "Ian Fisher" in browser.page_source


def test_can_visit_yayad_page(url, browser):
    browser.get(url + "/interns/yayad")
    assert "Yasmine Ayad" in browser.page_source
