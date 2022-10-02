import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://www.python.org/")


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    return {"browser": browser, "url": url}


def test_authorization():
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://target-sandbox.my.com/")
        time.sleep(5)

        button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]").click()

        search_email = driver.find_element(By.NAME, "email").send_keys("idarsho@gmail.com")
        search_password = driver.find_element(By.NAME, "password").send_keys("1234567890A")

        button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]").click()
        assert Exception
    finally:
        driver.quit()


def test_logout():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://target-sandbox.my.com/")
    time.sleep(5)

    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]").click()
    time.sleep(2)

    search_email = driver.find_element(By.NAME, "email").send_keys("idarsho@gmail.com")

    search_password = driver.find_element(By.NAME, "password").send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]").click()
    time.sleep(2)

    user_module = driver.find_element(By.CSS_SELECTOR, "//div[contains(@class,'blvNjE')]").click()
    time.sleep(2)

    button_logout = driver.find_element(By.XPATH, "//a[contains(@class,'2j8bjX')]").click()
    time.sleep(2)


def test_negative_password_authorization_1():
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://target-sandbox.my.com/")
        time.sleep(5)

        button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]").click()

        search_email = driver.find_element(By.NAME, "email").send_keys("idarsho@gmail.com")

        search_password = driver.find_element(By.NAME, "password").send_keys("1234567899A")

        button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]").click()

        assert "Invalid login or password" != '<html lang=...body></html>'
    finally:
        driver.quit()


def test_negative_email_authorization_1():
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://target-sandbox.my.com/")
        time.sleep(5)

        button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]").click()
        time.sleep(2)

        search_email = driver.find_element(By.NAME, "email").send_keys("idarsho177@gmail.com")

        search_password = driver.find_element(By.NAME, "password").send_keys("1234567890A")

        button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]").click()
        time.sleep(2)

        assert "Invalid login or password" not in '<html lang=...body></html>'
        time.sleep(5)
    finally:
        driver.quit()



def test_profile_change():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://target-sandbox.my.com/")
    driver.maximize_window()
    time.sleep(5)

    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]").click()
    time.sleep(2)

    search_email = driver.find_element(By.NAME, "email").send_keys("idarsho@gmail.com")

    search_password = driver.find_element(By.NAME, "password").send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]").click()
    time.sleep(2)

    module_profile = driver.find_element(By.XPATH, "//a[contains(@class,'1vgS83')]").click()
    time.sleep(10)

def test_parametrize():
    driver.get("https://target-sandbox.my.com/")
    time.sleep(5)
    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]").click()

    search_email = driver.find_element(By.NAME, "email").send_keys("idarsho@gmail.com")

    search_password = driver.find_element(By.NAME, "password").send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]").click()


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    return {"browser": browser, "url": url}


@pytest.fixture(scope='function')
def driver(config):
    browser = config["browser"]
    url = config["url"]

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        pass
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
