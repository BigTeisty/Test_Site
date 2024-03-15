from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class Tensor(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://tensor.ru/")

    def sila_v_lyudyakh(self):

        # self.find(By.XPATH, '//div[@class="tensor_ru-Index__block4-content"]//a[@href="/about"]').click()

        self.one = self.find(By.CLASS_NAME, 'tensor_ru-Index__block4-content')
        time.sleep(2)
        self.two = self.one.find_element(By.XPATH, '//a[@href="/about"]').click()
        return self.browser.current_url

    def same_size(self):

        time.sleep(2)
        element = self.browser.find_elements(By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img')

        test = {}
        i = 0
        for img in element:
            i += 1
            test[i] = img.size['height'], img.size['width']

        self.check = True
        tst = ''
        for ch in test:
            if tst != '' and tst != test[ch]:
                self.check = False
            tst = test[ch]

        return self.check