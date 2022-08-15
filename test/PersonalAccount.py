from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccount:

    def test_go_to_account_page(self, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки Войти в аккаунт
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки входа
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # локатор кнопки входа в личный Кабинет
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']"))
        )

        text = driver.find_element(By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']").text

        assert text == 'В этом разделе вы можете изменить свои персональные данные'

        driver.quit()

    def test_go_to_constructor_page(self, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки Войти в аккаунт
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки входа
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # локатор кнопки входа в личный Кабинет
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

        # локатор кнопки кoнструктор
        driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h1[text()='Соберите бургер']"))
        )

        text = driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").text

        assert text == 'Соберите бургер'

        driver.quit()

    def test_click_on_logo(self, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки Войти в аккаунт
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки входа
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # локатор кнопки входа в личный Кабинет
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

        # локатор логотипа Stellar Burgers
        driver.find_element(By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h1[text()='Соберите бургер']"))
        )

        text = driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").text

        assert text == 'Соберите бургер'

        driver.quit()

    def test_log_out_from_account(self, mail, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки Войти в аккаунт
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # поле "Email"
        driver.find_element(By.XPATH, "//*[text()='Email']/../input").send_keys(mail)

        # поле "Пароль"
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

        # локатор кнопки входа
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # локатор кнопки входа в личный Кабинет
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//button[text()='Выход']"))
        )

        # локатор кнопки кoнструктор
        driver.find_element(By.XPATH, "//button[text()='Выход']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h2[text()='Вход']"))
        )

        text = driver.find_element(By.XPATH, "//h2[text()='Вход']").text

        assert text == 'Вход'

        driver.quit()


personalAccount = TestPersonalAccount()

# personalAccount.test_go_to_account_page('sergei9196@ya.ru', 'e142456q')

# personalAccount.test_go_to_constructor_page('sergei9196@ya.ru', 'e142456q')

# personalAccount.test_click_on_logo('sergei9196@ya.ru', 'e142456q')

personalAccount.test_log_out_from_account('sergei9196@ya.ru', 'e142456q')


