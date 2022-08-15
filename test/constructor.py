from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_constructor_loaf(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки Соусы
        driver.find_element(By.XPATH, "//*[text()='Соусы']").click()

        # локатор кнопки Булки
        driver.find_element(By.XPATH, "//*[text()='Булки']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]"))
        )

        text = driver.find_element(By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]").text

        assert text == 'Булки'

        driver.quit()

    def test_constructor_sauces(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки входа в приложение
        driver.find_element(By.XPATH, "//*[text()='Соусы']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]"))
        )

        text = driver.find_element(By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]").text

        assert text == 'Соусы'

        driver.quit()

    def test_constructor_fillings(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        # локатор кнопки Начинки
        driver.find_element(By.XPATH, "//*[text()='Начинки']").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]"))
        )

        text = driver.find_element(By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]").text

        assert text == 'Начинки'

        driver.quit()


constructor = TestConstructor()

# constructor.test_constructor_loaf()

# constructor.test_constructor_sauces()

constructor.test_constructor_fillings()



