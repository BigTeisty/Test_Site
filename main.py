from selenium import webdriver
from pages.sbis import Sbis
from pages.tensor import Tensor
import pytest
import time

@pytest.fixture()
def browser():

    mbrowser = webdriver.Firefox()
    mbrowser.implicitly_wait(10)
    return mbrowser

def test_sbis(browser):

    sbis = Sbis(browser)
    sbis.open()
    sbis.click_kontact()
    sbis.click_img().click()
    time.sleep(10)
    browser.close()
    browser.quit()

def test_tensor(browser):

    tensor = Tensor(browser)
    tensor.open()
    tensor.sila_v_lyudyakh()
    assert "https://tensor.ru/about" == browser.current_url
    tensor.same_size()
    time.sleep(10)
    browser.close()
    browser.quit()

def test_sbis_two(browser):

    sbis = Sbis(browser)
    sbis.open()
    sbis.click_kontact()
    sbis.region()
    sbis.smena_regiona()
    sbis.region()
    sbis.url_title()
    time.sleep(10)
    browser.close()
    browser.quit()


