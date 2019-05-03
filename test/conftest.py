"""Definition of fixtures for pytest."""
import os

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


@pytest.fixture(scope="session")
def browser():
    """Get a (session-scoped) Selenium browser instance."""
    try:
        browser = webdriver.Firefox()
    except WebDriverException:
        browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def url():
    """Get the URL of the server currently being tested."""
    return os.environ["TEST_URL"]
