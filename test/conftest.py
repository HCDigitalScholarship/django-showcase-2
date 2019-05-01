"""Definition of fixtures for pytest."""
import os

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    """Get a (session-scoped) Selenium browser instance."""
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


@pytest.fixture
def url():
    """Get the URL of the server currently being tested."""
    return os.environ["TEST_URL"]
