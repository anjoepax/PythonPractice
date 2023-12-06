"""
Testing for assertpy library
"""
import time

from assertpy import assert_that
from selenium import webdriver


def start_chrome_browser():
    driver = webdriver.Chrome()
    driver.get("https://askomdch.com")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()


def start_remote_webdriver():
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub"
    )


def test_something():
    assert_that(1 + 2, description="Verify number is equal:").is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')


start_chrome_browser()
test_something()
