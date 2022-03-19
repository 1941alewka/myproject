from selenium.webdriver.common.by import By


class Locators:

    @staticmethod
    def getLocator(selector:str):
        return f"//table//div[contains(@class, 'PaQdxb A2W7l')]/div[contains(text(),'{selector}')]"

    @staticmethod
    def getLocatorfunc(selector:str):
        return f"//table//div[contains(@class, 'PaQdxb mF5fo')]/div[contains(text(),'{selector}')]"

    LOCATOR_RESULT = "//div/span[contains(@class,'qv3Wpe')]"
    LOCATOR_FUNC = "//div/span[contains(@class,'vUGUtc')]"
