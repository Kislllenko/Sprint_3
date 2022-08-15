from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogIn:

    def test_log_in_main_page(self, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки Войти в аккаунт
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки Войти
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[text()='Оформить заказ']"))
        )

        text = driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").text

        assert text == 'Оформить заказ'

        driver.quit()

    def test_log_in_my_account_page(self, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки входа в Личный Кабинет
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки входа
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[text()='Оформить заказ']"))
        )

        text = driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").text

        assert text == 'Оформить заказ'

        driver.quit()

    def test_log_in_throw_registration_page(self, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')

        # локатор кнопки входа в приложение
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки входа
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[text()='Оформить заказ']"))
        )

        text = driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").text

        assert text == 'Оформить заказ'

        driver.quit()

    def test_log_in_throw_password_recovery_page(self, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')

        # локатор кнопки восстановить пароль
        driver.find_element(By.XPATH, "//a[text()='Восстановить пароль']").click()

        # локатор кнопки входа в приложение
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки входа
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[text()='Оформить заказ']"))
        )

        text = driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").text

        assert text == 'Оформить заказ'

        driver.quit()


logIn = TestLogIn()

# logIn.test_log_in_main_page('sergei9196@ya.ru', 'e142456q')

# logIn.test_log_in_my_account_page('sergei9196@ya.ru', 'e142456q')

# logIn.test_log_in_throw_registration_page('sergei9196@ya.ru', 'e142456q')

logIn.test_log_in_throw_password_recovery_page('sergei9196@ya.ru', 'e142456q')

