import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://target-sandbox.my.com/")
    parser.addoption('--headless', action='store_true')


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    return {"browser": browser, "url": url, "headless": headless}


@pytest.fixture(scope='function')
def driver(config):
    browser = config["browser"]
    url = config["url"]

    if browser == "chrome":
        browser_options = Options()
        browser_options.headless = config["headless"]
        browser_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=browser_options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    time.sleep(7)
    driver.maximize_window()
    yield driver
    driver.quit()
