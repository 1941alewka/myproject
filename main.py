import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class Driver:

    def __init__(self):
        self.ser = Service("C:\\Users\\lexabicepz\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=self.ser)


class Func(Driver):

    def get_url(self, url):
        driver = self.driver
        driver.get(url)
        self.check_load_page(num=1, selector='q')

    def check_load_page(self, num: int, selector: str):
        """
        Проверяем, что страница прогрузилась

        :param num - выбираем по чему будем искать селектор
        :param selector - сам селектор

        """
        delay = 3
        try:
            selecot_data = {1: By.NAME, 2: By.ID, 3: By.CLASS_NAME}
            for key, value in selecot_data.items():
                if num == key:
                    myElem = WebDriverWait(self.driver, delay).until(
                        EC.presence_of_element_located((f'{value}', selector)))
                    print(f"Страница прогрузилась")
        except TimeoutException:
            print
            ("Страница долго грузится, либо не прогрузилась")

    def down(self):
        self.driver.close()
        self.driver.quit()

    def search(self):
        """
        Поиск в гугле
        """
        elem = self.driver.find_element(By.NAME, "q")
        elem.send_keys("Калькулатор")
        elem.send_keys(Keys.RETURN)

    def input(self):
        """
        Вводим данные в Калькулятор, считаем. Проверяем, что элементы отображаются на странице
        """

        self.check_load_page(num=2, selector='cwos')
        elem = self.driver.find_element(By.ID, "cwos")
        elem.click()
        data = ['1', '×', '2', '−', '3', '+', '1', '=']
        for i in data:
            if i == '×':
                elem = self.driver.find_element(By.XPATH, Locators.getLocatorfunc(i))
            elif i == '+':
                elem = self.driver.find_element(By.XPATH, Locators.getLocatorfunc(i))
            elif i == '=':
                elem = self.driver.find_element(By.XPATH, Locators.getLocatorfunc(i))
            elif i == '−':
                elem = self.driver.find_element(By.XPATH, Locators.getLocatorfunc(i))
            else:
                elem = self.driver.find_element(By.XPATH, Locators.getLocator(i))

            elem.click()
            if elem.is_displayed():
                print(f"Элемент {i} отображается на странице")
            else:
                print(f"Элемент {i}  НЕ отображается на странице")
            time.sleep(0.1)

    def check_result(self):
        """
        Проверяем, что результат верный + проверяем что отображается функция и результат
        """

        elem = self.driver.find_element(By.XPATH, Locators.LOCATOR_RESULT)
        assert elem.is_displayed(), 'Проверка, что результат виден'
        res = elem.text
        assert int(res) == 0, 'Проверка, что результат = 0 '
        elem2 = self.driver.find_element(By.XPATH, Locators.LOCATOR_FUNC)
        assert elem2.is_displayed(), 'Проверка, что наша функция отображается'
        func = elem2.text
        assert func == '1 × 2 - 3 + 1 =', f'Проверка, что данные функции совпадают'
