
from selenium.webdriver.support.ui import WebDriverWait as Wait   # импорт ожидания
from selenium.webdriver.support import expected_conditions as EC  # импорт Умного ожидания (где сколько необходимо)


class BasePage:  # базовый класс, от которо будут наследоваться остальные страницы

    def __init__(self, driver, url):  # при открытии любой страницы обязательно нужны драйвер и url
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):   # видимость элемента
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))   # драйвер, подожди 5 секунд, пока этот элемент не будет виден


    def element_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))  # драйвер, подожди 5 секунд, пока эти элементы не будут видны

    def remove_footer(self):   # удаление лишнего подвала сайта, который скрывает кнопку Submit
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementsByTagName('div')[4].remove();")
        self.driver.execute_script("document.getElementsByTagName('div')[5].remove();")


