from time import localtime, strftime, sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from xlutils.copy import copy as xlcopy
from datetime import *
import os
import json
import xlrd
import xlwt
import hashlib
import shutil
import dateutil.relativedelta


class Browser(object):
    """
    Methods for working with browser
    """
    def __init__(self, driver, timeout=60, log=True):
        self.driver = driver
        self.timeout = timeout
        self.data = Date
        self.log = log
        self.wait = Wait(self.driver, self.timeout)
        self.checker = Checker(self.driver, self.timeout)

    def set_value(self, locator, value, label=""):
        if value:
            element = self.wait.element_appear(locator)
            element.click()
            element.clear()
            element.send_keys(value)
            if label:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def clear_date_field(self, locator):
        element = self.wait.element_appear(locator)
        # element.click()
        element.send_keys('\b\b\b\b\b\b\b\b' + Keys.ENTER)

    #
    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(ec.alert_is_present())
            self.driver.switch_to_alert().accept()
        except TimeoutException:
            pass

    #
    def decline_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(ec.alert_is_present())
            self.driver.switch_to_alert().decline()
        except TimeoutException:
            pass

    # Click по локатору(Пример: (By.XPATH, "//input[@id='documentNumber']"))
    def click(self, locator, label=None):
        self.wait.loading()
        element = self.wait.element_appear(locator)
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait.loading()
        if label:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), label))

    # Click по тексту для кнопки или ссылки по тексту
    def click_by_text(self, text, order=1, exactly=False):
        self.wait.loading()
        if exactly:
            locator = (By.XPATH, "(//*[self::a or self::button][normalize-space()='%s'])[%s]" % (text, order))
        else:
            locator = (By.XPATH,
                       "(//*[self::a or self::button][contains(normalize-space(), '%s')])[%s]" % (text, order))
        element = self.wait.element_appear(locator)
        self.move_to_element(element)
        element.click()
        if text and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), text))

    # Click по атрибуту объекта на странице
    def click_by_value(self, value, order=1, exactly=False):
        self.wait.loading()
        if exactly:
            locator = (By.XPATH, "(//input[@value='%s'])[%s]" % (value, order))
        else:
            locator = (By.XPATH, "(//input[contains(@value, '%s')])[%s]" % (value, order))
        element = self.wait.element_appear(locator)
        self.move_to_element(element)
        element.click()
        if value and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), value))

    # выбор меню
    def click_menu(self, locator):
        sleep(1)
        element = self.driver.find_element_by_xpath(locator[1])
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()

    # Функция перехода на страницу
    def go_to(self, url):
        while self.driver.current_url != url:
            self.driver.get(url)
            sleep(.1)
        print("Переход по ссылке: %s" % url)

    # Функция скролирования до элемента
    def move_to_element(self, element):
        self.wait.loading()
        webdriver.ActionChains(self.driver).move_to_element(element).perform()

    # Функция скролирования вверх страницы
    def scroll_to_top(self):

        self.wait.loading()
        self.driver.execute_script("window.scrollTo(0, 0);")

    # Функция скролирования вниз страницы
    def scroll_to_bottom(self):

        self.wait.loading()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Функция скролирования модального окна вверх
    def scroll_modal_to_top(self, class_name='modal-body mCustomScrollbar', order=1):
        """
        Method for scrolling to top modal window
        :param class_name: tag class of modal window. there is value by default. change it if tag is different
        :param order: order in case of few modal windows. order starts from 0. that's why there is decreasing by 1
        :return:
        """
        self.wait.element_appear((By.XPATH, "//*[@class='{0}']".format(class_name)))
        self.driver.execute_script("""
               var modal = document.getElementsByClassName('%s')[%s];
               modal.scrollTo(0, 0);
           """ % (class_name, order - 1))

    # Функция скролирования модального окна вниз
    def scroll_modal_to_bottom(self, class_name='modal-body mCustomScrollbar', order=1):
        """
        Method for scrolling to bottom modal window
        :param class_name: tag class of modal window. there is value by default. change it if tag is different
        :param order: order in case of few modal windows. order starts from 0. that's why there is decreasing by 1
        :return:
        """
        self.wait.element_appear((By.XPATH, "//*[@class='{0}']".format(class_name)))
        self.driver.execute_script("""
               var modal = document.getElementsByClassName('%s')[%s];
               modal.scrollTo(0, modal.scrollHeight);
           """ % (class_name, order - 1))

    # Функция поиска строки в таблице по текстовому полю "Все поля"
    def search(self, value, label=""):
        self.wait.loading()
        element = self.driver.find_elements_by_xpath("//*[@placeholder='Все поля']")
        order = len(element)
        elements = self.driver.find_element_by_xpath("(//input[@placeholder='Все поля'])[%s]" % order)
        elements.send_keys(value + Keys.RETURN)
        self.wait.loading()
        print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def search_old(self, value):
        elements = self.driver.find_element_by_xpath("(//*[@placeholder='Все поля'])[last()]")
        elements.send_keys(value + Keys.RETURN)
        self.wait.loading()

    # Функция очистка поисковой строки если выбрано несколько фильтров
    def select2_clear(self, locator):
        self.wait.loading()
        element = self.wait.element_appear(locator)
        while True:
            try:
                element.click()
            except (ec.StaleElementReferenceException, ec.NoSuchElementException):
                break

    # Функция заполнение поля через троеточие(выбор из справочника)
    def set_type(self, locator, value, label=None):
        if value:
            element = self.wait.element_appear(locator).find_element(By.XPATH, ".//following-sibling::*[1]/button[2]")
            element.click()
            self.wait.loading()
            sleep(3)
            self.search(value)
            self.click_by_name("Выбрать")
            if label:
                print("[%s] [%s] выбор из справочника значения \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    def set_type2(self, locator, value, label=""):
        if value:
            element = self.wait.element_appear(locator).find_element(By.XPATH, ".//following-sibling::*[1]/button[2]")
            element.click()
            sleep(1)
            self.table_select_row_click(value)
            self.click_by_name("Выбрать")
            if label:
                print("[%s] [%s] выбор из справочника значения \"%s\"" % (strftime("%H:%M:%S",
                                                                                   localtime()), label, value))

    def set_type_alt(self, value, label=""):
        self.wait.loading()
        if value:
            sleep(1)
            self.search(value)
            self.click_by_name("Выбрать")
            if label:
                print("[%s] [%s] выбор из справочника значения \"%s\"" % (strftime("%H:%M:%S",
                                                                                   localtime()), label, value))

    # Функция заполнения текстового поля
    def set_text(self, locator, value, label=None):
        if value:
            self.wait.loading()
            element = self.wait.element_appear(locator)
            element.clear()
            element.send_keys(value)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))


    # Функция заполнения поля Дата
    def set_date(self, locator, value, label=None):
        if value:
            if value == "=":
                value = Date.get_today_date()
            self.wait.loading()
            element = self.wait.element_appear(locator)
            element.clear()
            sleep(1)
            element.send_keys(value+ Keys.RETURN)
            # element.send_keys(value + Keys.TAB)
            if label and self.log:
                print(
                    "[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция заполнения поля Дата
    def set_date_cut(self, locator, value, label=""):
        if value:
            element = self.wait.element_appear(locator)
            element.clear()
            element.send_keys(value + Keys.RETURN)
            element.send_keys(Keys.TAB)
            WebDriverWait(self.driver, self.timeout).until(
                ec.invisibility_of_element_located((By.ID, "ui-datepicker-div")))
            if label:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_dropdown(self, locator, value, label=""):
        if value:
            element = self.wait.element_appear(locator)
            element.click()
            self.click((By.XPATH, "//li[text()='%s']" % value))
            if label:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция заполнения текстового поля и проверка содержимого
    def set_text_and_check(self, locator, value, label=None):
        if value:
            self.wait.loading()
            element = self.wait.element_appear(locator)
            element.clear()
            element.send_keys(value)
            self.wait.lamb(lambda x: element.get_attribute("value") == value)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция заполнения/снятия чек-бокса
    def set_checkbox(self, locator, value=True, label=None):
        self.wait.loading()
        element = self.wait.element_appear(locator)
        if element.is_selected() != value:
            self.move_to_element(element)
            element.click()
            self.wait.loading()
            if label and self.log:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    # Функция заполнения/снятия чек-бокса без локатора
    def set_checkbox_wl(self, name, value=True, label=None, order=1):
        locator = (By.XPATH, "(//*[@name='%s'])[%s]//input" % (name, order))
        element = self.wait.element_appear(locator)
        if element.is_selected() != value:
            self.move_to_element(element)
            element.click()
            if label:
                pass
            else:
                label = self.driver.find_element_by_xpath("(//label[@for='%s'])[%s]" % (name, order)).text
            if label and self.log:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    # Функция(общая) заполнения/снятия чек-бокса по порядку элемента на страницу
    def set_checkbox_by_order(self, order=1, value=True, label=None):
        element = self.wait.element_appear((By.XPATH, "(//input[@type='checkbox'])[%s]" % order))
        if element.is_selected() != value:
            self.move_to_element(element)
            element.click()
            if label and self.log:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    # Функция заполнения/снятия радио-баттон
    def set_radio(self, locator, label=None):
        element = self.wait.element_appear(locator)
        element.click()
        if label and self.log:
            print("[%s] [%s] выбор опции" % (strftime("%H:%M:%S", localtime()), label))

    # Функция выбора значения из выпадающего списка
    def set_select(self, value, label=""):
        if value:
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located((By.XPATH, "//select[contains(., '%s')]" % value)))
            Select(element).select_by_visible_text(value)
            if label:
                print(
                    "[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция поиска строки в таблице по текстовому полю "Все поля"
    def search_string2(self, value, label=None):
        self.wait.loading()
        self.set_text((By.XPATH, "//*[@placeholder='Все поля']"), value + Keys.RETURN, label)
        if label and self.log:
            print(
                "[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    # Функция поиска строки в таблице по 2 аттрибутам
    def search_by_two_attributes(self, value, value2, flag=True,  order=1):
        self.wait.loading()
        locator = (By.XPATH, "(//tr[contains(., '%s')][contains(., '%s')]"
                             "//input[@type='checkbox'])[%s]" % (value, value2, order))
        self.set_checkbox(locator, flag)
        print(
            "[%s] Выбор строки с аттрибутами \"%s\" и \"%s\"" % (strftime("%H:%M:%S", localtime()), value, value2))



    # Функция выбора строки в таблице и нажатие на неё
    def table_select_row_click(self, text, order=1, label=None):
        self.wait.loading()
        locator = (By.XPATH, "(//tr[contains(., '%s')])[%s]" % (text, order))
        self.click(locator, label)

    # Функция выбора строки в таблице  и проставление чек-бокса
    def table_select_row(self, text, flag=True,  order=1, label=None):
        self.wait.loading()
        locator = (By.XPATH, "(//tr[contains(., '%s')]//input[@type='checkbox'])[%s]" % (text, order))
        self.set_checkbox(locator, flag, label)

    # Функция проставления всех чек-боксов в таблице
    def table_choose_all_checkbox(self, label=None):
        self.wait.loading()
        sleep(1)
        locator = (By.XPATH, "(//*[@class='w2ui-col-header  ']//input)")
        self.set_checkbox(locator, label)
        sleep(1)

    # Функция выбора чек-бокса в таблице по порядку
    """def table_row_checkbox(self, order=1):
        self.wait.loading()
        sleep(1)
        locator = (By.XPATH, "(//td/input[@type='checkbox'])[%s]" % order)
        self.set_checkbox(locator, True)
        sleep(1)
    """
    # Функция выбора радио-баттон в таблице по порядку
    def table_row_radio(self, order=1):
        self.wait.loading()
        sleep(1)
        locator = (By.XPATH, "(//td/input[@type='radio'])[%s]" % order)
        self.set_radio(locator)
        sleep(1)

    # Функция загрузки файла
    def upload_file(self, value, order=1):
        self.wait.loading()
        # открываем страницу с формой загрузки файла
        element = self.driver.find_element(By.XPATH, "(//input[@type='file'])[%s]" % order)

        element.clear()
        element.send_keys("%s/%s" % (os.getcwd(), value))
        WebDriverWait(self.driver, 60).until(
            ec.visibility_of_element_located((By.XPATH, "//li[@class=' qq-upload-success']")))

    # Функция выбор месяца
    def select_month(self, month, year):
        self.click((By.XPATH, "//button[@class='period-text dropdown-period-toggle']"))
        sleep(1)
        self.click((By.XPATH, "//*[span='%s']" % month))
        sleep(1)
        self.click((By.XPATH, "//*[span='%s']" % year))
        sleep(1)
        self.click((By.XPATH, "//span[@class='qa-icon-close']"))

    def save_screenshot(self, name, default_folder="", overwrite=True):
        """
        Method making screenshot of current page of driver
        :param name: Name of file. Extension is png by default
        :param default_folder: Folder with script by default. Important: use raw-strings if you using different one
        :param overwrite: Overwite file if True
        :return:
        """
        if os.path.isfile("%s%s.png" % (default_folder, name)):
            if overwrite:
                self.driver.save_screenshot("%s%s.png" % (default_folder, name))
            else:
                for i in range(100):
                    if not os.path.isfile("%s%s-%s.png" % (default_folder, name, i + 1)):
                        self.driver.save_screenshot("%s%s-%s.png" % (default_folder, name, i + 1))
                        break
        else:
            self.driver.save_screenshot("%s%s.png" % (default_folder, name))

    # Функция проверки текста в классе. Параметры: value - ожидаемый результат, class_name - имя класса, в котором
    # будет извлечен текст, text_errors - текст ошибки, который будет записан в файл logs.txt
    def checking_text_by_class(self, value, class_name, text_errors):
        find_value = self.driver.find_element_by_class_name(class_name).text
        if value == find_value:
            return True
        else:
            File.add_text_in_file("logs", text_errors)
            return False

    # Проверка текста в локаторе с записью в логфайл
    def check_text_and_logfile(self, locator, value, text_error):
        if self.wait.element_appear(locator).text == value:
            return True
        else:
            File.add_text_in_file("logs", text_error + str(value))
            return False

    def click_by_name(self, value, order=None):
        self.wait.loading()
        if not order:
            elements = self.driver.find_elements_by_xpath(
                "//*[self::button or self::span][contains(normalize-space(), '%s')]" % value)
            element = elements[Date.list_items_amount(elements) - 1]
        else:
            element = self.wait.element_appear(
                (By.XPATH, "(//*[self::button or self::span][contains(normalize-space(), '%s')])[%s]" % (value, order)))
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        if value:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), value))
            self.wait.loading()

    def click_on_employee(self, value):
        element = self.wait.element_appear((By.XPATH, "//*[self::a or self::span][.='%s']" % value))
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait.loading()
        if value:
            print("[%s] [%s] нажатие на сотрудника" % (strftime("%H:%M:%S", localtime()), value))


class Date(object):
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
    """
    Methods for working with date
    """
    # Функция возвращающая текущую дату
    @staticmethod
    def get_today_date():
        return datetime.today().strftime("%d.%m.%Y")

    @staticmethod
    def get_today_file():
        return datetime.today().strftime("%Y%m%d")

    @staticmethod
    def get_date(date):
        if date:
            month = year = 0
            l = date.split('.')
            if l[1] != '=':
                month = int(l[1])
            if l[2] != '=':
                year = int(l[2])
            dt = Date.change_month(datetime.today().replace(day=int(l[0])), 12 * year + month)
            return '%s.%s.%s' % (dt.day, dt.month, dt.year)
        else:
            return date

    @staticmethod
    def list_items_amount(list):
        amount = 0
        for i in list:
            amount += 1
        return amount

    @staticmethod
    def change_month(date, amount=0):
        return date + dateutil.relativedelta.relativedelta(months=amount)

    @staticmethod
    def get_mmyy(date):
        if date:
            l = date.split('.')
            year = 0
            if l[1] != '=':
                year = int(l[1])
            return '%s%s' % (l[0], datetime.today().year % 2000 + year)
        else:
            return date


class Wait(object):
    """
    Methods for waiting
    """
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    # Функция ожидания текста пока не появится
    def text_appear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    # Функция ожидания пока текст не пропадёт
    def text_disappear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    # Функция ожидания элемента пока не появится  в скрытых
    def presence_of_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))

    # Функция ожидания элемента пока не появится
    def element_appear(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator))

    # Функция ожидания пока элемент не пропадёт
    def element_disappear(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.invisibility_of_element_located(locator))

    def lamb(self, exe):
        return WebDriverWait(self.driver, self.timeout).until(exe)

    # Функция ожидания окончания закгрузки - пока не пропал лоадер
    def loading(self):
        WebDriverWait(self.driver, self.timeout).until(
            ec.invisibility_of_element_located((By.XPATH, "//div[@class='gifPreloader ng-scope']")))
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//div[@class='windows8']")))
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//div[@class='w2ui-lock']")))
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//div[@id='loadingSpinner']")))


# Проверка текста
class Checker(object):
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.wait = Wait(self.driver, self.timeout)

    # Проверка текста без локатора в input или textarea(поля ввода) в атрибуте title
    def check_text_title(self, name, value):
        actual_value = self.wait.element_appear(
            (By.XPATH, "//*[@name='%s']//*[self::input or self::textarea]" % name)).get_attribute("title")
        print('[%s]Проверка...' % strftime("%H:%M:%S", localtime()))
        print("Ф:{%s}" % actual_value)
        print("О:{%s}" % str(value))
        if actual_value == value:
            print("[%s] СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return True
        else:
            print("[%s] НЕ СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return False

    # Проверка текста без локатора в input или textarea(поля ввода) в атрибуте value
    def check_text_input(self, name, value, order=1):
        element = self.wait.element_appear(
            (By.XPATH, "(//*[@name='%s'])[%s]//*[self::input or self::textarea]" % (name, order)))
        actual_value = element.get_attribute("value")
        print('[%s]Проверка...' % strftime("%H:%M:%S", localtime()))
        print("Ф:{%s}" % actual_value)
        print("О:{%s}" % str(value))
        if actual_value == value:
            print("[%s] СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return True
        else:
            print("[%s] НЕ СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return False

    # Проверка текста без локатора в select(поле выбора из справочника)
    def check_text_select(self, name, value, order=1):
        element = self.wait.element_appear(
            (By.XPATH, "(//*[@name='%s'])[%s]//li" % (name, order)))
        actual_value = element.get_attribute("title")
        print('[%s]Проверка...' % strftime("%H:%M:%S", localtime()))
        print("Ф:{%s}" % actual_value)
        print("О:{%s}" % str(value))
        if actual_value == value:
            print("[%s] СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return True
        else:
            print("[%s] НЕ СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return False

    # Проверка текста c локатором в input

    def check_text_locator(self, locator, value):
        element = self.wait.element_appear(locator)
        actual_value = element.get_attribute("value")
        print('[%s]Проверка...' % strftime("%H:%M:%S", localtime()))
        print("Ф:{%s}" % actual_value)
        print("О:{%s}" % str(value))
        if actual_value == value:
            print("[%s] СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return True
        else:
            print("[%s] НЕ СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return False

    # Проверка текста без локатора в input

    def check_text(self, name, value, order=1):
        element = self.wait.element_appear(
            (By.XPATH, "(//*[@name='%s'])[%s]//input" % (name, order)))
        actual_value = element.get_attribute("value")
        print('[%s]Проверка...' % strftime("%H:%M:%S", localtime()))
        print("Ф:{%s}" % actual_value)
        print("О:{%s}" % str(value))
        if actual_value == value:
            print("[%s] СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return True
        else:
            print("[%s] НЕ СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return False

    # Проверка сообщения

    def check_message(self, value):
        element = self.wait.element_appear(
            (By.XPATH, "//document-execution-result/div"))
        actual_value = ' '.join(element.text.split('\n'))
        print('[%s]Проверка...' % strftime("%H:%M:%S", localtime()))
        print("Ф:{%s}" % actual_value)
        print("О:{%s}" % str(value))
        if actual_value == value:
            print("[%s] СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return True
        else:
            print("[%s] НЕ СООТВЕТСТВУЕТ" % strftime("%H:%M:%S", localtime()))
            return False

    # Функция поиска строки в таблице по 2 аттрибутам
    def search_by_two_attributes_info(self, value, value2):
        self.wait.loading()
        try:
            element = self.wait.element_appear((
                By.XPATH, "//tr[@line and contains(., '{0}') and contains(., '{1}')]".format(value, value2)))
            print(
                "[%s] ПРОВЕРКА СТРОКИ! Найдена строка с аттрибутами \"%s\" и \"%s\"" % (
                    strftime("%H:%M:%S", localtime()), value, value2))
        except TimeoutException:
            print("Doesnt exist")


# Работа с данными
class Data(object):
    """
    Methods for working with data
    """
    @staticmethod
    def load_data(file):
        script_path = os.path.dirname(__file__)
        filename = os.path.join(script_path, 'data\\%s.json' % file)
        return json.loads(open(filename, encoding="utf8").read())

    @staticmethod
    def get_data_by_value(data, parent, key, value):
        for i in data[parent]:
            if value == i[key]:
                return i
        return None

    @staticmethod
    def get_data_by_number(data, parent, number=0):
        return data[parent][number]


class File(object):
    """
    Методы для работы с файлами
    """
    # Добавление текста в файл
    @staticmethod
    def add_text_in_file(filename, text):
        with open(filename + ".txt") as my_file:
            tmp = my_file.read()
        with open(filename + ".txt", "w") as my_file:
            my_file.write(tmp + "\n" + text)

    @staticmethod
    def file_copy(filename):
        test_default = ('C:\\Users\\' + os.getlogin() + '\\Downloads\\')
        test_buch = "C:\\TestBuch\\"
        # Проверка наличия папки C:\TestBuch
        if os.access(test_buch, os.F_OK):
            pass
        else:
            os.mkdir(test_buch)
        # Проверка наличия папки C:\Users\'Доменное имя пользователя'\Downloads
        if os.access(test_default, os.F_OK):
            pass
        else:
            os.mkdir(test_default)
        # os.chdir(test_buch)
        path = Date.get_today_file()
        # Проверка наличия папки с датой проведения теста
        if os.access(test_buch+path, os.F_OK):
            pass
        else:
            os.mkdir(test_buch+path)
        # os.chdir(test_default)
        # Копируем полученную печатную форму в отдельный каталог C:\TestBuch
        shutil.copy2(test_default + filename, test_buch + path)
        test_buch_date = test_buch + path + "\\"
        if os.access(test_buch_date+path + filename, os.F_OK):
            os.remove(test_buch_date+path + filename)
        os.rename(test_buch_date+filename, test_buch_date + path + filename)
        if os.access(test_default + "example.xls", os.F_OK):
            pass
        else:
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("Лист1")
            sheet.write(0, 0, 'Тест')
            workbook.save(test_default + "example.xls")
        if os.access(test_default + "example_new.xls", os.F_OK):
            pass
        else:
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("Лист1")
            sheet.write(0, 0, 'Тест')
            workbook.save(test_default + "example_new.xls")

    @staticmethod
    def get_max_rows_and_cols(file):
        rows_max = 0
        cols_max = 0
        for name in file.sheet_names():
            sheet = file.sheet_by_name(name)
            if rows_max < sheet.nrows:
                rows_max = sheet.nrows
            if cols_max < sheet.ncols:
                cols_max = sheet.ncols
        return [rows_max, cols_max]

    # Сравнение excel файлов 1
    @staticmethod
    def analyze_two_files(filename):
        test_default = 'C:\\Users\\' + os.getlogin() + '\\Downloads\\'
        test_compare = 'C:\\Compare_zrp\\'
        File.file_copy(filename)
        reference_file = test_default + filename
        output_file = test_compare + filename
        # output_hash = self.md5(output_file)
        # reference_hash = self.md5(reference_file)
        # открываем исходный файл
        output = xlrd.open_workbook(output_file, on_demand=True, formatting_info=True)
        reference = xlrd.open_workbook(reference_file, on_demand=True, formatting_info=True)
        if output.nsheets != reference.nsheets:
            print('Количество книг не совпадает')
        else:
            output_max = File.get_max_rows_and_cols(output)
            reference_max = File.get_max_rows_and_cols(reference)
            max_rows = max(reference_max[0], output_max[0])
            max_cols = max(reference_max[1], output_max[1])

            reference_new = xlcopy(reference)
            for i in range(reference.nsheets):
                sheet = reference_new.get_sheet(i)
                sheet.write(max_rows, max_cols, "!")
            reference_new.save(test_default + "example.xls")
            output_new = xlcopy(output)
            for i in range(output.nsheets):
                sheet = output_new.get_sheet(i)
                sheet.write(max_rows, max_cols, "!")
            output_new.save(test_default + "example_new.xls")
            return [test_default + "example.xls", test_default + "example_new.xls"]

    @staticmethod
    def compare_files(filename):
        files = File.analyze_two_files(filename)
        test_default = ('C:\\Users\\' + os.getlogin() + '\\Downloads\\')
        reference = xlrd.open_workbook(files[0], on_demand=True, formatting_info=True)
        output = xlrd.open_workbook(files[1], on_demand=True, formatting_info=True)
        flag = True
        print("[%s] ПРОВЕРКА ПЕЧАТНОЙ ФОРМЫ : \"%s\"" % (strftime("%H:%M:%S", localtime()), filename))
        for index in range(reference.nsheets):
            reference_sheet = reference.sheet_by_index(index)
            output_sheet = output.sheet_by_index(index)
            reference_sheet_name = reference_sheet.name
            output_sheet_name = output_sheet.name
            if reference_sheet_name != output_sheet_name:
                print("Название книги[%s] не совпадает с эталонным [%s]!" % (output_sheet_name, reference_sheet_name))
            for i in range(reference_sheet.nrows):
                for j in range(reference_sheet.ncols):
                    reference_cell = reference_sheet.cell(i, j).value
                    output_cell = output_sheet.cell(i, j).value
                    if reference_cell != output_cell:
                        if flag:
                            flag = False
                        print("Книга [%s]:" % reference_sheet_name)
                        print("\tЯчейка [%s, %s]. Значение [%s] не совпадает с эталонным [%s]!"
                              % (i+1, j+1, reference_cell, output_cell))
        reference.release_resources()
        output.release_resources()
        del reference
        del output
        if flag:
            print("[%s] Печатные формы одинаковы" % (strftime("%H:%M:%S", localtime())))
        os.remove(test_default + "example.xls")
        os.remove(test_default + "example_new.xls")

    # Получение хеша
    @staticmethod
    def md5(filename):
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def checking_file_export_ufk():
        test_default = ('C:\\Users\\' + os.getlogin() + '\\Downloads\\')
        flag = True
        for file in os.listdir(test_default):
            if file.endswith(".ZR3"):
                print("[%s] Фаил с именем [%s] Выгружен" % (strftime("%H:%M:%S", localtime()), file))
                flag = False
            if file.endswith(".ZS3"):
                print("[%s] Фаил с именем [%s] Выгружен" % (strftime("%H:%M:%S", localtime()), file))
                flag = False
        if flag:
            print("[%s] Файлов выгрузки не найдено" % strftime("%H:%M:%S", localtime()))
