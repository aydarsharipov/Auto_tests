import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope='function', autouse=True)
def test_authorization():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://target-sandbox.my.com/")
    time.sleep(5)

    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()

    search_email = driver.find_element(By.NAME, "email")
    search_email.send_keys("idarsho@gmail.com")
    search_password = driver.find_element(By.NAME, "password")
    search_password.send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    time.sleep(4)
    title_text = driver.find_element(By.XPATH, "//div[contains(@class,'right-module-userNameWrap-3Odw2D')]")
    if title_text.text == "idarsho@gmail.com":
        print("Мы попали на главную страницу")

    driver.close()

def test_logout():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://target-sandbox.my.com/")
    time.sleep(5)

    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()
    time.sleep(2)

    search_email = driver.find_element(By.NAME, "email").send_keys("idarsho@gmail.com")

    search_password = driver.find_element(By.NAME, "password").send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    time.sleep(3)

    button_profile = driver.find_element(By.XPATH, "//div[contains(@class,'3e-duF')]").click()
    time.sleep(2)
    button_logout = driver.find_element(By.XPATH, "//a[contains(@href,'/logout')]").click()
    time.sleep(2)
    driver.close()


@pytest.mark.parametrize("email, password, result", [("idarshogmail.com", "1234567890A", "Введите email или телефон"), ("idarsho@gmail.com", "1239567899A", "Invalid login or password")])
def test_negative_authorization_1(email, password, result):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://target-sandbox.my.com/")
    time.sleep(5)

    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()

    search_email = driver.find_element(By.NAME, "email")
    search_email.send_keys(email)
    search_password = driver.find_element(By.NAME, "password")
    search_password.send_keys(password)
    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    assert result in driver.page_source
    driver.close()




def test_profile_change():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://target-sandbox.my.com/")
    driver.maximize_window()
    time.sleep(5)

    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()
    time.sleep(2)

    search_email = driver.find_element(By.NAME, "email")
    search_email.send_keys("idarsho@gmail.com")

    search_password = driver.find_element(By.NAME, "password")
    search_password.send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    time.sleep(2)

    module_profile = driver.find_element(By.XPATH,
                                         "//a[contains(@class,'center-module-button-14O4yB center-module-profile-1kuUOa')]")
    module_profile.click()
    time.sleep(5)

    phone_number = driver.find_element(By.XPATH, "// input[contains(@maxlength, '20')]")
    phone_number.clear()
    phone_number.send_keys("+79167000154")

    save_button = driver.find_element(By.XPATH, "// button[contains(@class, 'button button_submit')]")
    save_button.click()
    time.sleep(2)

    assert "Информация успешно сохранена" in driver.page_source

    driver.quit()


@pytest.mark.parametrize("section, xpath, result", [('balance', '//a[contains(@class,"center-module-button-14O4yB center-module-billing-1cIfj4")]', '//input[contains(@class,"deposit__payment-form__submit js-deposit-payment-submit")]'), ('profile', '//a[contains(@class,"center-module-button-14O4yB center-module-profile-1kuUOa")]', '// button[contains(@class, "button button_submit")]')])
def test_parametrize_1(section, xpath, result):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://target-sandbox.my.com/")
    driver.maximize_window()
    time.sleep(5)

    button_input = driver.find_element(By.XPATH, "//div[contains(@class,'2yl51i')]")
    button_input.click()

    search_email = driver.find_element(By.NAME, "email")
    search_email.send_keys("idarsho@gmail.com")

    search_password = driver.find_element(By.NAME, "password")
    search_password.send_keys("1234567890A")

    button_login = driver.find_element(By.XPATH, "//div[contains(@class,'1u2DYF')]")
    button_login.click()
    time.sleep(3)

    module_statistics = driver.find_element(By.XPATH, "//a[contains(@class,'center-module-button-14O4yB center-module-statistics-2Wbrwh')]")
    module_statistics.click()
    time.sleep(5)

    module_section = driver.find_element(By.XPATH, xpath)
    module_section.click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, result)
    driver.quit()
