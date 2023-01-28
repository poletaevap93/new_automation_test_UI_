import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):

    def fill_fields_and_submit(self):
        person = generated_person()
        path = generated_file()
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)  # send_keys(first_name) - заполняем поле нашем именем
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)  #в поле кликаем как enter (зашито в логику поля)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
        os.remove(path)   # запрос операционке об удалении файла , чтоб не копились
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(Locators.SUBMIT).click()
        return person

    def form_result(self):  # метод, который будет возвращать результат итоговой таблицы
        result_list = self.element_are_visible(Locators.RESULT_TABLE)    #здесь хранится список элементов из получившейся таблицы, именно со второй части таблицы, где только значения

        result_text = [i.text for i in result_list]   # здесь в новый массив через цикл for помещаю текст, который хранится в result_list
        return result_text