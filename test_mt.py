import pytest
from selenium.webdriver.common.by import By


def test_authorization(driver):
    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()

    search_email = driver.find_element(By.NAME, "email")
    search_email.send_keys("idarsho@gmail.com")
    search_password = driver.find_element(By.NAME, "password")
    search_password.send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()


def test_logout(driver):
    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()
    driver.implicitly_wait(10)

    driver.find_element(By.NAME, "email").send_keys("idarsho@gmail.com")

    driver.find_element(By.NAME, "password").send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    driver.implicitly_wait(10)

    button_profile = driver.find_element(By.XPATH, "//div[contains(@class,'3e-duF')]")
    button_profile.click()
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//a[contains(@href,'/logout')]").click()


@pytest.mark.parametrize(
    "email, password, result",
    [
        (
         "idarshogmail.com",
         "1234567890A",
         "Please input email or mobile phone number",
        ),
        (
         "idarsho@gmail.com",
         "1239567899A",
         "Invalid login or password"
        ),
    ],)
def test_negative_authorization_1(driver, email, password, result):
    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()

    search_email = driver.find_element(By.NAME, "email")
    search_email.send_keys(email)
    search_password = driver.find_element(By.NAME, "password")
    search_password.send_keys(password)
    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    driver.implicitly_wait(10)
    assert result in driver.page_source


def test_profile_change(driver):
    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()
    driver.implicitly_wait(10)

    search_email = driver.find_element(By.NAME, "email")
    search_email.send_keys("idarsho@gmail.com")

    search_password = driver.find_element(By.NAME, "password")
    search_password.send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    driver.implicitly_wait(10)

    module_profile = driver.find_element(
        By.XPATH,
        "//a[contains(@class,'center-module-button-14O4yB center-module-profile-1kuUOa')]",
    )
    module_profile.click()
    driver.implicitly_wait(10)

    phone_number = driver.find_element(By.XPATH, "// input[contains(@maxlength, '20')]")
    phone_number.clear()
    phone_number.send_keys("+79167000154")

    save_button = driver.find_element(
        By.XPATH, "// button[contains(@class, 'button button_submit')]"
    )
    save_button.click()
    driver.implicitly_wait(10)

    assert "Информация успешно сохранена" in driver.page_source


@pytest.mark.parametrize(
    "section, xpath, result",
    [
        (
            "balance",
            '//a[contains(@class,"center-module-button-14O4yB center-module-billing-1cIfj4")]',
            '//input[contains(@class,"deposit__payment-form__submit js-deposit-payment-submit")]',
        ),
        (
            "profile",
            '//a[contains(@class,"center-module-button-14O4yB center-module-profile-1kuUOa")]',
            '// button[contains(@class, "button button_submit")]',
        ),
    ],
)
def test_parametrize_1(driver, section, xpath, result):
    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()

    search_email = driver.find_element(By.NAME, "email")
    search_email.send_keys("idarsho@gmail.com")

    search_password = driver.find_element(By.NAME, "password")
    search_password.send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    driver.implicitly_wait(10)

    module_statistics = driver.find_element(
        By.XPATH,
        "//a[contains(@class,'center-module-button-14O4yB center-module-statistics-2Wbrwh')]",
    )
    module_statistics.click()
    driver.implicitly_wait(10)

    module_section = driver.find_element(By.XPATH, xpath)
    module_section.click()
    driver.implicitly_wait(10)

    assert driver.find_element(By.XPATH, result)
