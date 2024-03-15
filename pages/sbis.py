from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class Sbis(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://sbis.ru/")

    def click_kontact(self):
        time.sleep(4)
        return self.find(By.LINK_TEXT, 'Контакты').click()

    def click_img(self):
        time.sleep(2)
        return self.find(By.XPATH, '//a[@title="tensor.ru"]')

    ########2 test

    def region(self):
        self.ob_informaciya = self.find(By.XPATH, '//*[@class="controls-ListViewV controls_list_theme-sbisru controls-ListView_default controls-itemActionsV_menu-hidden"]').text
        self.reg = self.find(By.CSS_SELECTOR, '.ml-16 > span:nth-child(1)').text
        self.city = self.find(By.CSS_SELECTOR, '#city-id-2').text
        return self.reg, self.city, self.ob_informaciya

    def smena_regiona(self):
        time.sleep(2)
        self.find(By.CSS_SELECTOR, '.ml-16 > span:nth-child(1)').click()
        time.sleep(2)
        self.find(By.XPATH, '//li[@class="sbis_ru-Region-Panel__item"]//*[@title="Камчатский край"]').click()

    def url_title(self):
        self.url = self.browser.current_url
        self.title = self.browser.title
        return self.title, self.url