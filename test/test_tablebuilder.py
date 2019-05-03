"""
Functional tests for the tablebuilder app.

These tests use Selenium, a library that lets you control a browser with Python. We use
Selenium to test the user interface and JavaScript.
"""
from helper import wait_for


def test_can_add_new_row_and_save_it(url, browser):
    browser.get(url + "/tablebuilder/")

    # Find the table and make sure there's only one row in it.
    table = browser.find_element_by_id("table")
    assert len(table.find_elements_by_css_selector("tr")) == 1

    # Find the add button, click it, and wait until another row appears.
    add_button = browser.find_element_by_id("add-button")
    add_button.click()
    wait_for(lambda: len(table.find_elements_by_css_selector("tr")) == 2)

    # Fill each input in the new row with the string "Haverford".
    row = browser.find_element_by_css_selector("tr:nth-child(1)")
    for elem in row.find_elements_by_css_selector("input"):
        elem.send_keys("Haverford")

    # Save the row and wait for the inputs to disappear.
    save_button = row.find_element_by_css_selector("button.save-button")
    save_button.click()
    wait_for(lambda: len(row.find_elements_by_css_selector("input")) == 0)

    # Check that our input got put in the saved row.
    for cell in row.find_elements_by_css_selector(".content-cell"):
        assert "Haverford" in cell.text


def test_add_several_rows(url, browser):
    browser.get(url + "/tablebuilder/")

    # Find the table and make sure there's only one row in it.
    table = browser.find_element_by_id("table")
    assert len(table.find_elements_by_css_selector("tr")) == 1

    # Find the add button, click it, and wait until another row appears.
    add_button = browser.find_element_by_id("add-button")
    add_button.click()
    wait_for(lambda: len(table.find_elements_by_css_selector("tr")) == 2)

    # Fill each input in the new row with the string "Haverford".
    row = browser.find_element_by_css_selector("tr:nth-child(1)")
    for elem in row.find_elements_by_css_selector("input"):
        elem.send_keys("Haverford")

    # Save the row and wait for the inputs to disappear.
    save_button = row.find_element_by_css_selector("button.save-button")
    save_button.click()
    wait_for(lambda: len(row.find_elements_by_css_selector("input")) == 0)

    # Check that our input got put in the saved row.
    for cell in row.find_elements_by_css_selector(".content-cell"):
        assert "Haverford" in cell.text

    # Add two more rows.
    add_button.click()
    wait_for(lambda: len(table.find_elements_by_css_selector("tr")) == 3)
    add_button.click()
    wait_for(lambda: len(table.find_elements_by_css_selector("tr")) == 4)

    row = browser.find_element_by_css_selector("tr:nth-child(3)")
    for elem in row.find_elements_by_css_selector("input"):
        elem.send_keys("Scholarship")

    save_button = row.find_element_by_css_selector("button.save-button")
    save_button.click()
    wait_for(lambda: len(row.find_elements_by_css_selector("input")) == 0)

    for cell in row.find_elements_by_css_selector(".content-cell"):
        assert "Scholarship" in cell.text

    row = browser.find_element_by_css_selector("tr:nth-child(2)")
    for elem in row.find_elements_by_css_selector("input"):
        elem.send_keys("Digital")

    save_button = row.find_element_by_css_selector("button.save-button")
    save_button.click()
    wait_for(lambda: len(row.find_elements_by_css_selector("input")) == 0)

    for cell in row.find_elements_by_css_selector(".content-cell"):
        assert "Digital" in cell.text


def test_add_and_edit_a_row(url, browser):
    browser.get(url + "/tablebuilder/")

    add_some_rows(browser, ["JavaScript"])

    row = browser.find_element_by_css_selector("tr:nth-child(1)")
    edit_button = browser.find_element_by_css_selector("button.edit-button")
    edit_button.click()
    wait_for(lambda: len(row.find_elements_by_css_selector("input")) != 0)

    for elem in row.find_elements_by_css_selector("input"):
        assert "JavaScript" in elem.get_attribute("value")
        elem.clear()
        elem.send_keys("Python")

    save_button = row.find_element_by_css_selector("button.save-button")
    save_button.click()
    wait_for(lambda: len(row.find_elements_by_css_selector("input")) == 0)

    for cell in row.find_elements_by_css_selector(".content-cell"):
        assert "Python" in cell.text
        assert "JavaScript" not in cell.text


def test_add_and_cancel_editing_a_row(url, browser):
    browser.get(url + "/tablebuilder/")

    add_some_rows(browser, ["JavaScript"])

    row = browser.find_element_by_css_selector("tr:nth-child(1)")
    edit_button = browser.find_element_by_css_selector("button.edit-button")
    edit_button.click()
    wait_for(lambda: len(row.find_elements_by_css_selector("input")) != 0)

    for elem in row.find_elements_by_css_selector("input"):
        assert "JavaScript" in elem.get_attribute("value")
        elem.clear()
        elem.send_keys("Python")

    cancel_button = row.find_element_by_css_selector("button.cancel-button")
    cancel_button.click()
    wait_for(lambda: len(row.find_elements_by_css_selector("input")) == 0)

    for cell in row.find_elements_by_css_selector(".content-cell"):
        assert "JavaScript" in cell.text
        assert "Python" not in cell.text


def test_remove_row(url, browser):
    browser.get(url + "/tablebuilder/")

    add_some_rows(browser, ["Haverford", "Bryn Mawr", "Swarthmore", "Penn"])

    row = browser.find_element_by_css_selector("tr:nth-child(4)")
    remove_button = row.find_element_by_css_selector("button.remove-button")
    remove_button.click()
    wait_for(lambda: "Penn" not in browser.page_source)

    table = browser.find_element_by_id("table")
    assert len(table.find_elements_by_css_selector("tr")) == 4


def add_some_rows(browser, content):
    nrows = 1
    table = browser.find_element_by_id("table")
    add_button = browser.find_element_by_id("add-button")
    for cell in content:
        add_button.click()
        wait_for(lambda: len(table.find_elements_by_css_selector("tr")) == nrows + 1)
        nrows += 1

        # Fill each input in the new row with the string "Haverford".
        row = browser.find_element_by_css_selector("tr:nth-child({})".format(nrows - 1))
        for elem in row.find_elements_by_css_selector("input"):
            elem.send_keys(cell)

        save_button = row.find_element_by_css_selector("button.save-button")
        save_button.click()
        wait_for(lambda: len(row.find_elements_by_css_selector("input")) == 0)
