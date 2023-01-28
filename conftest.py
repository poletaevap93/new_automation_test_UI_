import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture() # декоратор
def driver():
    driver_service = Service(ChromeDriverManager().install())   # создаю сервис
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()  #открытие окна сразу на все окно
    yield driver   # все, что выше этой строки - будет выполняться ПЕРЕД тестом, ниже - ПОСЛЕ
    driver.quit()