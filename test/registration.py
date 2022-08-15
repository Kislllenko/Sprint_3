from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_input_correct_registration_data(self, name, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки входа в аккаунт
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # локатор кнопки Зарегистрироваться
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        # поле "Имя"
        driver.find_element(By.XPATH, "//*[text()='Имя']/../input").send_keys(name)

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки Зарегистрироваться после ввода имени, логина и пароля
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h2[text()='Вход']"))
        )

        text = driver.find_element(By.XPATH, "//h2[text()='Вход']").text

        assert text == 'Вход'

        driver.quit()

    def test_input_incorrect_registration_data(self, name, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки Войти в аккаунт
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # локатор кнопки Зарегистрироваться
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        # поле "Имя"
        driver.find_element(By.XPATH, "//*[text()='Имя']/../input").send_keys(name)

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки Зарегистрироваться после ввода имени, логина и пароля
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//p[@class='input__error text_type_main-default']"))
        )

        text = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text

        assert text == 'Некорректный пароль'

        driver.quit()


registration = TestRegistration()

# registration.test_input_correct_registration_data('sergei24567', 'sergei9196@ya.ru', 'e142456q')

registration.test_input_incorrect_registration_data('sergei24567', 'sergei9196@ya.ru', 'e1424')
