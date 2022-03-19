import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Driver:

    def __init__(self):
        self.ser = Service("C:\\Users\\lexabicepz\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=self.ser)

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
        data = ['1', '×', '2', '−', '3','+', '1','=']
        for i in data:
            xpath_num = f"//table//div[contains(@class, 'PaQdxb A2W7l')]/div[contains(text(),'{i}')]"
            xpath_func = f"//table//div[contains(@class, 'PaQdxb mF5fo')]/div[contains(text(),'{i}')]"
            if i == '×':
                elem = self.driver.find_element(By.XPATH, xpath_func)
            elif i == '+':
                elem = self.driver.find_element(By.XPATH, xpath_func)
            elif i == '=':
                elem = self.driver.find_element(By.XPATH, xpath_func)
            elif i == '−':
                elem = self.driver.find_element(By.XPATH, xpath_func)
            else:
                elem = self.driver.find_element(By.XPATH, xpath_num)

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
        xpath_res = "//div/span[contains(@class,'qv3Wpe')]"
        xpath_up = "//div/span[contains(@class,'vUGUtc')]"
        elem = self.driver.find_element(By.XPATH, xpath_res)
        assert elem.is_displayed(), 'Проверка, что результат виден'
        res = elem.text
        assert int(res) == 0, 'Проверка, что результат = 0 '
        elem2 = self.driver.find_element(By.XPATH, xpath_up)
        assert elem2.is_displayed(),'Проверка, что наша функция отображается'
        func = elem2.text
        assert func == '1 × 2 - 3 + 1 =', f'Проверка, что данные функции совпадают'


if __name__ == "__main__":
    dr = Driver()
    dr.get_url(url="https://www.google.com")
    dr.search()
    dr.input()
    dr.check_result()
    dr.down()
