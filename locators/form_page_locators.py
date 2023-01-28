from selenium.webdriver.common.by import By
from random import randint

class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')        # f'for="hobbies-checkbox-{randint(1,3)}"' - с помощью рандома можем с каждым тестом выбирать разные варианты радиобатона, от 1 до 3 варианта
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECT = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')
    FILE_INPUT = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')