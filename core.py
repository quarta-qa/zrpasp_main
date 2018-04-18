from time import sleep, localtime, strftime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from locators import *
from setup import *
from datetime import *
import dateutil.relativedelta

TIMEOUT = 30


def get_date(date):
    if date:
        month = year = 0
        l = date.split('.')
        if l[1] != '=':
            month = int(l[1])
        if l[2] != '=':
            year = int(l[2])
        dt = change_month(datetime.today().replace(day=int(l[0])), 12*year+month)
        return '%s.%s.%s' % (dt.day, dt.month, dt.year)
    else:
        return date

def list_items_amount(list):
    amount = 0
    for i in list:
        amount += 1
    return amount

def change_month(date, amount=0):
    return date + dateutil.relativedelta.relativedelta(months=amount)


def get_mmyy(date):
    if date:
        l = date.split('.')
        year = 0
        if l[1] != '=':
            year = int(l[1])
        return '%s%s' % (l[0], datetime.today().year % 2000 + year)
    else:
        return date


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def set_value(self, locator, value, label=""):
        if value:
            element = self.wait(locator)
            element.click()
            element.clear()
            element.send_keys(value)
            if label:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def clear_date_field(self, locator):
        element = self.wait(locator)
        #element.click()
        element.send_keys('\b\b\b\b\b\b\b\b' + Keys.ENTER)

    def set_date(self, locator, value, label=""):
        if value:
            element = self.wait(locator)
            element.clear()
            element.send_keys(value + Keys.RETURN)
            # element.send_keys(Keys.TAB)
            WebDriverWait(self.driver, TIMEOUT).until(EC.invisibility_of_element_located((By.ID, "ui-datepicker-div")))
            if label:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_date_cut(self, locator, value, label=""):
        if value:
            element = self.wait(locator)
            element.clear()
            element.send_keys(value + Keys.RETURN)
            element.send_keys(Keys.TAB)
            WebDriverWait(self.driver, TIMEOUT).until(EC.invisibility_of_element_located((By.ID, "ui-datepicker-div")))
            if label:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_dropdown(self, locator, value, label=""):
        if value:
            element = self.wait(locator)
            element.click()
            self.click((By.XPATH, "//li[text()='%s']" % value))
            if label:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_checkbox(self, locator, value, label=""):
        element = self.wait(locator)
        if element.is_selected() != value:
            element.click()
            self.wait_for_loading()
            if label:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    def search_old(self, value):
        elements = self.driver.find_element_by_xpath("(//*[@placeholder='Все поля'])[last()]")
        elements.send_keys(value + Keys.RETURN)
        self.wait_for_loading()

    def search(self, value):
        element = self.driver.find_elements_by_xpath("//*[@placeholder='Все поля']")
        order = len(element)
        elements = self.driver.find_element_by_xpath("(//input[@placeholder='Все поля'])[%s]" % order)
        elements.send_keys(value + Keys.RETURN)
        self.wait_for_loading()

    def table_select_row_click(self, text, order=1, label=None):
        self.wait_for_loading()
        locator = (By.XPATH, "(//tr[contains(., '%s')])[%s]" % (text, order))
        self.click(locator, label)

    def set_type(self, locator, value, label=""):
        if value:
            element = self.wait(locator).find_element(By.XPATH, ".//following-sibling::*[1]/button[2]")
            element.click()
            self.wait_for_loading()
            sleep(5)
            self.search(value)
            self.click_by_name("Выбрать")
            if label:
                print("[%s] [%s] выбор из справочника значения \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    def set_type2(self, locator, value, label=""):
        if value:
            element = self.wait(locator).find_element(By.XPATH, ".//following-sibling::*[1]/button[2]")
            element.click()
            sleep(1)
            self.table_select_row_click(value)
            self.click_by_name("Выбрать")
            if label:
                print("[%s] [%s] выбор из справочника значения \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    def move_to_element(self, element):
        self.wait_for_loading()
        webdriver.ActionChains(self.driver).move_to_element(element).perform()

    def set_type_alt(self, value, label=""):
        if value:
            self.search(value)
            self.click_by_name("Выбрать")
            if label:
                print("[%s] [%s] выбор из справочника значения \"%s\"" % (strftime("%H:%M:%S",
                                                                                   localtime()), label, value))

    def set_select(self, value, label=""):
        if value:
            element = WebDriverWait(self.driver, TIMEOUT).until(
                EC.visibility_of_element_located((By.XPATH, "//select[contains(., '%s')]" % value)))
            Select(element).select_by_visible_text(value)
            if label:
                print(
                    "[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def click(self, locator, label=None):
        self.wait_for_loading()
        element = self.wait(locator)
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait_for_loading()
        if label:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), label))

    # def click_by_name(self, value, order=1):
    #
    #     self.wait_for_loading()
    #     element = self.wait((By.XPATH, "(//*[self::button or self::span][contains(normalize-space(), '%s')])[%s]" % (value, order)))
    #     webdriver.ActionChains(self.driver).move_to_element(element).perform()
    #     element.click()
    #     self.wait_for_loading()
    #     if value:
    #         print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), value))

    def click_by_name(self, value, order=None):
        self.wait_for_loading()
        if not order:
            elements = self.driver.find_elements_by_xpath(
                "//*[self::button or self::span][contains(normalize-space(), '%s')]" % value)
            element = elements[list_items_amount(elements)-1]
        else:
            element = self.wait(
                (By.XPATH, "(//*[self::button or self::span][contains(normalize-space(), '%s')])[%s]" % (value, order)))
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        if value:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), value))
            self.wait_for_loading()

    def click_on_employee(self, value):
        element = self.wait((By.XPATH, "//*[self::a or self::span][.='%s']" % value))
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait_for_loading()
        if value:
            print("[%s] [%s] нажатие на сотрудника" % (strftime("%H:%M:%S", localtime()), value))

    def wait(self, locator):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(locator))


    def wait_for_loading(self):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='gifPreloader ng-scope']")))
        WebDriverWait(self.driver, TIMEOUT).until_not(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='windows8']")))
        WebDriverWait(self.driver, TIMEOUT).until_not(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='w2ui-lock']")))
        WebDriverWait(self.driver, TIMEOUT).until_not(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='loadingSpinner']")))



class LoginPage(BasePage):

    def open(self):
        self.driver.get(Links.login_page)

    def username(self, value):
        self.set_value(LoginLocators.username, value, "Логин")

    def password(self, value):
        self.set_value(LoginLocators.password, value, "Пароль")

    def lot(self, value):
        self.set_dropdown(LoginLocators.lot, value, "Участок")

    # def date(self, value):
    #     self.set_date(LoginLocators.date, value, "")

    def submit(self):
            self.click(LoginLocators.submit, "Войти")

    def login(self, data):
        self.username(data["username"])
        self.password(data["password"])
        self.lot(data["lot"])
        self.submit()


class MainPage(BasePage):

    def open(self):
        self.driver.get(Links.main_page)
        self.wait_for_loading()

    def logout(self):
        self.click(MainLocators.logout, "Пикторграмма выхода")
        self.wait(LoginLocators.username)


class Menu(BasePage):

    def open(self):
        sleep(1)
        self.click(MenuLocators.menu_icon, "Главное меню")

    def catalogs(self):
        sleep(1)
        self.click(MenuLocators.catalogs, "Справочники")

    def employees(self):
        sleep(1)
        self.click(MenuLocators.employees, "Сотрудники")

    def documents(self):
        sleep(1)
        self.click(MenuLocators.documents, "Документы")

    def subdivision_structure(self):
        sleep(1)
        self.click(MenuLocators.subdivision_structure, "Структура подразделений")

    def disabled(self):
        sleep(1)
        self.click(MenuLocators.disabled, "Структура подразделений")


class EmployeesPage(BasePage):

    def add(self):
        self.click(EmployeesLocators.add, "Добавить")

    def select_employee(self, value):
        self.search(value)
        self.click_on_employee(value)


class EmployeeCardPage(BasePage):

    def open(self):
        self.click(EmployeeCardLocators.edit_button, "Редактировать")

    def last_name(self, value):
        self.set_value(EmployeeCardLocators.last_name, value, "Фамилия")

    def first_name(self, value):
        self.set_value(EmployeeCardLocators.first_name, value, "Имя")

    def middle_name(self, value):
        self.set_value(EmployeeCardLocators.middle_name, value, "Отчество")

    def gender(self, value):
        self.set_select(value, "Пол")

    def birthday(self, value):
        self.set_date(EmployeeCardLocators.birthday, value, "Дата рождения")

    def submit(self):
        self.click(EmployeeCardLocators.submit, "Сохранить")

    def submit2(self):
        self.click(EmployeeCardLocators.submit2, "Сохранить")

    def submit3(self):
        self.click(EmployeeCardLocators.submit3, "Сохранить")

    def save(self):
        self.click(EmployeeCardLocators.save, "Сохранить")

    def dialog_save(self):
        self.click(EmployeeCardLocators.dialog_save, "Сохранить")

    def tariff_salary(self, value):
        self.set_type2(EmployeeCardLocators.tariff_salary, value, "Начисление для окалада/тарифа")


class PersonalAccountPage(BasePage):

    def open(self):
        self.click(PersonalAccountLocators.tab)

    def add(self):
        self.click(PersonalAccountLocators.add, "Добавить")

    def new_member(self):
        self.open()
        self.add()


class AccountInfoPage(BasePage):

    def open(self):
        self.click(AccountInfoLocators.tab)

    def personnel_number(self, value):
        self.set_value(AccountInfoLocators.personnel_number, value, "Табельный номер")

    def receipt_date(self, value):
        self.set_date(AccountInfoLocators.receipt_date, get_date(value), "Дата приема")

    def order_number(self, value):
        self.set_value(AccountInfoLocators.order_number, value, "Номер приказа")

    def salary_amount(self, value):
        self.set_value(AccountInfoLocators.salary_amount, value, "Сумма оклада")

    def working_hours(self, value):
        self.set_value(AccountInfoLocators.working_hours, value, "Продолжительность рабочего дня")

    def change_date(self, value):
        self.set_date(AccountInfoLocators.change_date, value, "Дата последнего изменения оклада")

    def payment_category(self, value):
        self.set_select(value, "Категория оплаты")

    def payment_category_by(self, value):
        self.set_select(value, "Категория работника по затратам")

    def time_category(self, value):
        self.set_select(value, "Категория рабочего времени")

    def status_on(self, value):
        self.set_date(AccountInfoLocators.status_on, value, "Дата установки статуса")

    def status_off(self, value):
        self.set_date(AccountInfoLocators.status_off, value, "Дата окончания статуса")

    def ets(self, value):
        self.set_select(value, "Разряд ЕТС")

    def subdivision(self, value):
        self.set_type(AccountInfoLocators.subdivision, value, "Подразделение")

    def position(self, value):
        self.set_type(AccountInfoLocators.position, value, "Должность")

    def experience(self, value):
        self.set_date(AccountInfoLocators.experience, value, "Стаж гос. службы с")

    def last_payroll(self, value):
        self.set_value(AccountInfoLocators.last_payroll, value, "Последний расчет зарплаты")

    def dismissal_date(self, value):
        self.set_date(AccountInfoLocators.dismissal_date, value, "Дата увольнения")

    def fired(self, value):
        self.set_checkbox(AccountInfoLocators.fired, value, "Уволен")

    def dismissal_number(self, value):
        self.set_value(AccountInfoLocators.dismissal_number, value, "Номер приказа об увольнении")

    def employee_category(self, value):
        self.set_select(value, "Категория работника")

    def class_rank(self, value):
        self.set_type(AccountInfoLocators.class_rank, value, "Классный чин")

    def union_member(self, value):
        self.set_checkbox(AccountInfoLocators.union_member, value, "Член профсоюза")

    def member_from(self, value):
        self.set_date(AccountInfoLocators.member_from, value, "Член профсоюза с")

    def member_to(self, value):
        self.set_date(AccountInfoLocators.member_to, value, "Член профсоюза по")

    def employee_number(self, value):
        self.set_value(AccountInfoLocators.employee_number, value, "Табельный номер замещающего")

    def fill_page(self, data):
        self.personnel_number(data["personalAccount"]["accountInfo"]["personnelNumber"])
        self.receipt_date(data["personalAccount"]["accountInfo"]["receiptDate"])
        self.order_number(data["personalAccount"]["accountInfo"]["orderNumber"])
        self.salary_amount(data["personalAccount"]["accountInfo"]["salaryAmount"])
        self.working_hours(data["personalAccount"]["accountInfo"]["workingHours"])
        self.change_date(data["personalAccount"]["accountInfo"]["changeDate"])
        self.payment_category(data["personalAccount"]["accountInfo"]["paymentCategory"])
        self.payment_category_by(data["personalAccount"]["accountInfo"]["employeeCategoryBy"])
        self.time_category(data["personalAccount"]["accountInfo"]["timeCategory"])
        self.status_on(data["personalAccount"]["accountInfo"]["statusOn"])
        self.status_off(data["personalAccount"]["accountInfo"]["statusOff"])
        self.ets(data["personalAccount"]["accountInfo"]["ets"])
        self.subdivision(data["personalAccount"]["accountInfo"]["subdivision"])
        self.position(data["personalAccount"]["accountInfo"]["position"])
        self.experience(data["personalAccount"]["accountInfo"]["experience"])
        self.last_payroll(data["personalAccount"]["accountInfo"]["lastPayroll"])
        self.dismissal_date(data["personalAccount"]["accountInfo"]["dismissalDate"])
        self.fired(data["personalAccount"]["accountInfo"]["fired"])
        self.dismissal_number(data["personalAccount"]["accountInfo"]["dismissalNumber"])
        self.employee_category(data["personalAccount"]["accountInfo"]["employeeCategory"])
        self.class_rank(data["personalAccount"]["accountInfo"]["classRank"])
        self.union_member(data["personalAccount"]["accountInfo"]["unionMember"])
        self.member_from(data["personalAccount"]["accountInfo"]["memberFrom"])
        self.member_to(data["personalAccount"]["accountInfo"]["memberTo"])
        self.employee_number(data["personalAccount"]["accountInfo"]["employeeNumber"])


class CalcInfoPage(BasePage):

    def open(self):
        self.click(CalcInfoLocators.tab)

    def holiday_payment(self, value):
        self.set_select(value, "Расчет отпуска")

    def holiday_period_from(self, value):
        self.set_date(CalcInfoLocators.holiday_period_from, value, "Период отпуска с")

    def holiday_period_to(self, value):
        self.set_date(CalcInfoLocators.holiday_period_to, value, "Период отпуска по")

    def note(self, value):
        self.set_value(CalcInfoLocators.note, value, "Примечание")

    def sick_days_percent(self, value):
        self.set_select(value, "Процент больничного")

    def average_daily_earnings(self, value):
        self.set_value(CalcInfoLocators.average_daily_earnings, value, "Среднедневной заработок (CP1)")

    def privileges_type(self, value):
        self.set_select(value, "Тип льгот на сотрудника")

    def coefficient(self, value):
        self.set_value(CalcInfoLocators.coefficient, value, "Районный коэффициент")

    def state_employee(self, value):
        self.set_checkbox(CalcInfoLocators.state_employee, value, "Не госслужащий")

    def main_work(self, value):
        self.set_checkbox(CalcInfoLocators.main_work, value, "Неосновное место работы")

    def resident(self, value):
        self.set_checkbox(CalcInfoLocators.resident, value, "Не резидент")

    def pluralist(self, value):
        self.set_checkbox(CalcInfoLocators.pluralist, value, "Совместитель")

    def chaes_member(self, value):
        self.set_checkbox(CalcInfoLocators.chaes_member, value, "Участник ЧАЭС")

    def chaes_number(self, value):
        self.set_value(CalcInfoLocators.chaes_number, value, "Номер удостоверения участника ЧАЭС")

    def salary_without_rounding(self, value):
        self.set_checkbox(CalcInfoLocators.salary_without_rounding, value, "Выплата зарплаты без округления")

    def income_tax(self, value):
        self.set_checkbox(CalcInfoLocators.income_tax, value, "Удерживать налог на доходы")

    def prepaid_expense(self, value):
        self.set_checkbox(CalcInfoLocators.prepaid_expense, value, "Выплачивать аванс")

    def region(self, value):
        self.set_select(value, "Регион для почтового сбора")

    def alimony(self, value):
        self.set_select(value, "Уплата алиментов")

    def stb_card(self, value):
        self.set_checkbox(CalcInfoLocators.stb_card, value, "Выплата через STB-card")

    def payment_method(self, value):
        self.set_select(value, "Способ оплаты")

    def card_number(self, value):
        self.set_value(CalcInfoLocators.card_number, value, "Номер карты/счета в банке")

    def full_name(self, value):
        self.set_value(CalcInfoLocators.full_name, value, "ФИО на латинице")

    def validity(self, value):
        self.set_value(CalcInfoLocators.validity, get_mmyy(value), "Срок действия")

    def bank_list(self, value):
        self.set_value(CalcInfoLocators.bank_list, value, "Список (банк)")

    def key(self, value):
        self.set_value(CalcInfoLocators.key, value, "Ключ")

    def fill_page(self, data):
        self.holiday_payment(data["personalAccount"]["calcInfo"]["holidayPayment"])
        self.holiday_period_from(data["personalAccount"]["calcInfo"]["holidayPeriodFrom"])
        self.holiday_period_to(data["personalAccount"]["calcInfo"]["holidayPeriodTo"])
        self.note(data["personalAccount"]["calcInfo"]["note"])
        self.sick_days_percent(data["personalAccount"]["calcInfo"]["sickDaysPercent"])
        self.average_daily_earnings(data["personalAccount"]["calcInfo"]["averageDailyEarnings"])
        self.privileges_type(data["personalAccount"]["calcInfo"]["privilegesType"])
        self.coefficient(data["personalAccount"]["calcInfo"]["coefficient"])
        self.state_employee(data["personalAccount"]["calcInfo"]["stateEmployee"])
        self.main_work(data["personalAccount"]["calcInfo"]["mainWork"])
        self.resident(data["personalAccount"]["calcInfo"]["resident"])
        self.pluralist(data["personalAccount"]["calcInfo"]["pluralist"])
        self.chaes_member(data["personalAccount"]["calcInfo"]["chaesMember"])
        self.chaes_number(data["personalAccount"]["calcInfo"]["chaesNumber"])
        self.salary_without_rounding(data["personalAccount"]["calcInfo"]["salaryWithoutRounding"])
        self.income_tax(data["personalAccount"]["calcInfo"]["incomeTax"])
        self.prepaid_expense(data["personalAccount"]["calcInfo"]["prepaidExpense"])
        self.region(data["personalAccount"]["calcInfo"]["region"])
        self.alimony(data["personalAccount"]["calcInfo"]["alimony"])
        self.stb_card(data["personalAccount"]["calcInfo"]["stbCard"])
        self.payment_method(data["personalAccount"]["calcInfo"]["paymentMethod"])
        self.card_number(data["personalAccount"]["calcInfo"]["cardNumber"])
        self.full_name(data["personalAccount"]["calcInfo"]["fullName"])
        self.validity(data["personalAccount"]["calcInfo"]["validity"])
        self.bank_list(data["personalAccount"]["calcInfo"]["bankList"])
        self.key(data["personalAccount"]["calcInfo"]["key"])


class EmployeePrivilegesPage(BasePage):

    def open(self):
        self.click(EmployeePrivilegesLocators.tab)

    def add(self):
        self.click(EmployeePrivilegesLocators.add, "Добавить")

    def date_start(self, value):
        self.set_date(EmployeePrivilegesLocators.date_start, get_date(value), "Начало действия")

    def date_end(self, value):
        self.set_date(EmployeePrivilegesLocators.date_end, value, "Конец действия")

    def child_privilege(self, value):
        self.set_checkbox(EmployeePrivilegesLocators.child_privilege, value, "Льгота на детей и иждивенцев")

    def renouncement(self, value):
        self.set_checkbox(EmployeePrivilegesLocators.renouncement, value, "Отказ другого родителя")

    def child_number(self, value):
        self.set_value(EmployeePrivilegesLocators.child_number, value, "Порядковый номер ребенка")

    def statement_number(self, value):
        self.set_value(EmployeePrivilegesLocators.statement_number, value, "Номер заявления")

    def single_parent(self, value):
        self.set_checkbox(EmployeePrivilegesLocators.single_parent, value, "Одинокий родитель")

    def birthday(self, value):
        self.click(EmployeePrivilegesLocators.birthday)
        self.wait_for_loading()
        self.set_date(EmployeePrivilegesLocators.birthday, value, "Дата рождения")

    def statement_date(self, value):
        self.click(EmployeePrivilegesLocators.statement_date)
        self.wait_for_loading()
        self.set_date(EmployeePrivilegesLocators.statement_date, get_date(value), "Дата заявления")

    def disabled(self, value):
        self.set_checkbox(EmployeePrivilegesLocators.disabled, value, "Ребенок-инвалид")

    def tax_deduction(self, value):
        self.set_checkbox(EmployeePrivilegesLocators.tax_deduction, value, "Имущественный налоговый вычет")

    def tutor(self, value):
        self.set_checkbox(EmployeePrivilegesLocators.tutor, value, "Опекун")

    def professional_deduction(self, value):
        self.set_checkbox(EmployeePrivilegesLocators.professional_deduction, value, "Профессиональный вычет")

    def social_deduction(self, value):
        self.set_checkbox(EmployeePrivilegesLocators.social_deduction, value, "Социальный вычет")

    def note(self, value):
        self.set_value(EmployeePrivilegesLocators.note, value, "Примечание")

    def privileges_amount(self, value):
        self.set_value(EmployeePrivilegesLocators.privileges_amount, value,
                       "Количество льгот (только для льготы на сотрудника)")

    def deduction_code(self, value):
        self.set_type(EmployeePrivilegesLocators.deduction_code, value, "Код имущественного/социального вычета")

    def deduction_sum(self, value):
        self.set_value(EmployeePrivilegesLocators.deduction_sum, value, "Сумма имущественного/социального вычета")

    def imns(self, value):
        self.set_value(EmployeePrivilegesLocators.imns, value, "ИМНС (для имущественного/социального вычета)")

    def notification_number(self, value):
        self.set_value(
            EmployeePrivilegesLocators.notification_number, value,
            "Номер уведомления (для имущественного/социального вычета)")

    def notification_date(self, value):
        self.set_date(EmployeePrivilegesLocators.notification_date, value,
                      "Дата уведомления (для имущественного/социального вычета)")

    def submit(self):
        self.click(EmployeePrivilegesLocators.submit, "Сохранить")

    def fill_page(self, data):
        self.date_start(data["personalAccount"]["employeePrivileges"]["dateStart"])
        self.date_end(data["personalAccount"]["employeePrivileges"]["dateEnd"])
        if data["personalAccount"]["employeePrivileges"]["childPrivilege"]:
            self.child_privilege(data["personalAccount"]["employeePrivileges"]["childPrivilege"])
            self.renouncement(data["personalAccount"]["employeePrivileges"]["renouncement"])
            self.child_number(data["personalAccount"]["employeePrivileges"]["childNumber"])
            self.statement_number(data["personalAccount"]["employeePrivileges"]["statementNumber"])
            self.single_parent(data["personalAccount"]["employeePrivileges"]["singleParent"])
            self.birthday(data["personalAccount"]["employeePrivileges"]["birthday"])
            self.statement_date(data["personalAccount"]["employeePrivileges"]["statementDate"])
        self.disabled(data["personalAccount"]["employeePrivileges"]["disabled"])
        self.tax_deduction(data["personalAccount"]["employeePrivileges"]["taxDeduction"])
        self.professional_deduction(data["personalAccount"]["employeePrivileges"]["professionalDeduction"])
        self.social_deduction(data["personalAccount"]["employeePrivileges"]["socialDeduction"])
        self.note(data["personalAccount"]["employeePrivileges"]["note"])
        self.privileges_amount(data["personalAccount"]["employeePrivileges"]["privilegesAmount"])
        self.deduction_code(data["personalAccount"]["employeePrivileges"]["deductionCode"])
        self.deduction_sum(data["personalAccount"]["employeePrivileges"]["deductionSum"])
        self.imns(data["personalAccount"]["employeePrivileges"]["imns"])
        self.notification_number(data["personalAccount"]["employeePrivileges"]["notificationNumber"])
        self.notification_date(data["personalAccount"]["employeePrivileges"]["notificationDate"])


class WageIndexationPage(BasePage):

    def open(self):
        self.click_by_name("Сведения о лицевом счете")


class HistoryPage(BasePage):

    def open(self):
        self.click_by_name("Сведения о лицевом счете")


class DocumentsPage(BasePage):

    def open(self):
        self.click(DocumentsLocators.tab)

    def document_type(self, value):
        self.set_select(value, "Вид документа")

    def serial_number(self, value1, value2, value3):
        self.set_value(DocumentsLocators.serial_first, value1, "Серия 1")
        self.set_value(DocumentsLocators.serial_second, value2, "Серия 2")
        self.set_value(DocumentsLocators.serial_third, value3, "Номер")

    def department_code(self, value):
        self.set_value(DocumentsLocators.department_code, value, "Код подразделения")

    def issue_date(self, value):
        self.set_date(DocumentsLocators.issue_date, value, "Дата выдачи")

    def issued_by(self, value):
        self.set_value(DocumentsLocators.issued_by, value, "Выдан")

    def fill_page(self, data):
        self.document_type(data["documents"]["documentType"])
        self.serial_number(data["documents"]["serialFirst"],
                        data["documents"]["serialSecond"],
                        data["documents"]["serialThird"])
        self.department_code(data["documents"]["departmentCode"])
        self.issue_date(data["documents"]["issueDate"])
        self.issued_by(data["documents"]["issuedBy"])


class AddressesPage(BasePage):

    def open(self):
        self.click(AddressesLocators.tab)

    def index(self, value):
        self.set_value(AddressesLocators.index, value, "Индекс")

    def region(self, value):
        self.set_value(AddressesLocators.region, value, "Регион")

    def area(self, value):
        self.set_value(AddressesLocators.area, value, "Район")

    def area_type(self, value):
        self.set_type(AddressesLocators.area_type, value, "Тип района")

    def city(self, value):
        self.set_value(AddressesLocators.city, value, "Город")

    def city_type(self, value):
        self.set_type(AddressesLocators.city_type, value, "Тип города")

    def locality(self, value):
        self.set_value(AddressesLocators.locality, value, "Населенный пункт")

    def locality_type(self, value):
        self.set_type(AddressesLocators.locality_type, value, "Тип населенного пункта")

    def street(self, value):
        self.set_value(AddressesLocators.street, value, "Улица")

    def street_type(self, value):
        self.set_type(AddressesLocators.street_type, value, "Тип улицы")

    def building(self, value):
        self.set_value(AddressesLocators.building, value, "Дом")

    def block(self, value):
        self.set_value(AddressesLocators.block, value, "Корпус")

    def apartment(self, value):
        self.set_value(AddressesLocators.apartment, value, "Квартира")

    def use(self, value):
        self.set_checkbox(AddressesLocators.use, value, "Использовать КЛАДР")

    def actual_address(self, value):
        self.set_value(AddressesLocators.actual_address, value, "Адрес фактического проживания")

    def fill_page(self, data):
        self.index(data["addresses"]["index"])
        self.region(data["addresses"]["region"])
        self.area(data["addresses"]["area"])
        self.area_type(data["addresses"]["areaType"])
        self.city(data["addresses"]["city"])
        self.city_type(data["addresses"]["cityType"])
        self.locality(data["addresses"]["locality"])
        self.locality_type(data["addresses"]["localityType"])
        self.street(data["addresses"]["street"])
        self.street_type(data["addresses"]["streetType"])
        self.building(data["addresses"]["building"])
        self.block(data["addresses"]["block"])
        self.apartment(data["addresses"]["apartment"])
        self.use(data["addresses"]["use"])
        self.actual_address(data["addresses"]["actualAddress"])


class PFRPage(BasePage):

    def open(self):
        self.click(PFRLocators.tab)

    def registration_number(self, value):
        self.set_value(PFRLocators.registration_number, value, "Регистрационный номер в ПФ")

    def category(self, value):
        self.set_select(value, "Категория плательщика в ПФ")

    def locality_type(self, value):
        self.set_select(value, "Тип местности")

    def retirement_date(self, value):
        self.set_date(PFRLocators.retirement_date, value, "Дата выхода на пенсию")

    def esn(self, value):
        self.set_checkbox(PFRLocators.esn, value, "Расчет ЕСН для иностранцев")

    def last_name(self, value):
        self.set_value(PFRLocators.last_name, value, "Фамилия для ПФ")

    def first_name(self, value):
        self.set_value(PFRLocators.first_name, value, "Имя для ПФ")

    def middle_name(self, value):
        self.set_value(PFRLocators.middle_name, value, "Отчество для ПФ")

    def nationality(self, value):
        self.set_type(PFRLocators.nationality, value, "Гражданство ПФР")

    def exclude(self, value):
        self.set_checkbox(PFRLocators.exclude, value, "Исключить из отчета в ПФ (в/с)")

    def country(self, value):
        self.set_value(PFRLocators.country, value, "Страна")

    def region(self, value):
        self.set_value(PFRLocators.region, value, "Область")

    def area(self, value):
        self.set_value(PFRLocators.area, value, "Район")

    def city(self, value):
        self.set_value(PFRLocators.city, value, "Город/село")

    def fill_page(self, data):
        self.registration_number(data["pfr"]["registrationNumber"])
        self.category(data["pfr"]["category"])
        self.locality_type(data["pfr"]["localityType"])
        self.retirement_date(data["pfr"]["retirementDate"])
        self.esn(data["pfr"]["esn"])
        self.last_name(data["pfr"]["lastName"])
        self.first_name(data["pfr"]["firstName"])
        self.middle_name(data["pfr"]["middleName"])
        self.nationality(data["pfr"]["nationality"])
        self.exclude(data["pfr"]["exclude"])
        self.country(data["pfr"]["country"])
        self.region(data["pfr"]["region"])
        self.area(data["pfr"]["area"])
        self.city(data["pfr"]["city"])


class FNSPage(BasePage):

    def open(self):
        self.click(FNSLocators.tab)

    def itn(self, value):
        self.set_value(FNSLocators.itn, value, "ИНН")

    def exclude(self, value):
        self.set_checkbox(FNSLocators.exclude, value, "Исключить из отчета в ГНИ?")

    def resident(self, value):
        self.set_checkbox(FNSLocators.resident, value, "Не резидент?")

    def nationality(self, value):
        self.set_select(value, "Гражданство ГНИ")

    def fill_page(self, data):
        self.itn(data["fns"]["itn"])
        self.exclude(data["fns"]["exclude"])
        self.resident(data["fns"]["resident"])
        self.nationality(data["fns"]["nationality"])


class DisabledPage(BasePage):

    def add(self):
        self.click_by_name("Добавить")


class DisabledCardPage(BasePage):

    def full_name(self, value):
        self.wait(DisabledCardLocators.full_name).find_element(By.XPATH, ".//following-sibling::*[1]/button[2]").click()
        self.wait((By.XPATH, "//div[@class='w2ui-col-header ' and contains(., 'Имя')]"))
        self.set_type_alt(value, "Фамилия И.О.")

    def reference(self, value):
        self.set_value(DisabledCardLocators.reference, value, "Справка учреждения медико-социальной экспертизы")

    def reference_number(self, value):
        self.set_value(DisabledCardLocators.reference_number, value, "Номер справки")

    def date(self, value):
        self.set_date(DisabledCardLocators.date, get_date(value), "Дата выдачи")

    def group(self, value):
        self.set_value(DisabledCardLocators.group, value, "Группа инвалидности")

    def validity(self, value):
        self.set_value(DisabledCardLocators.validity, get_date(value), "Срок")


class FullNamePage(BasePage):

    def open(self):
        self.click(FullNameLocators.tab)


class OtherPage(BasePage):

    def open(self):
        self.click(OtherLocators.tab)

    def requisites(self, value):
        self.set_type(OtherLocators.requisites, value, "Банковские реквезиты")

    def phone_number(self, value):
        self.set_value(OtherLocators.phone_number, value, "Телефон")

    def email(self, value):
        self.set_value(OtherLocators.email, value, "E-Mail")

    def crimea(self, value):
        self.set_checkbox(OtherLocators.crimea, value, "Крым, Севастополь(для б/л)")

    def fill_page(self, data):
        self.requisites(data["other"]["requisites"])
        self.phone_number(data["other"]["phoneNumber"])
        self.email(data["other"]["email"])
        self.crimea(data["other"]["crimea"])


class PayrollWithholdingPage(BasePage):

    def prev_month(self):
        self.click(PayrollWithholdingLocators.prev_month, "Предыдущий месяц")

    def next_month(self):
        self.click(PayrollWithholdingLocators.next_month, "Следующий месяц")

    def add_payroll(self):
        self.click(PayrollWithholdingLocators.add, "Добавить")
        self.click(PayrollWithholdingLocators.payroll, "Начисление")

    def add_withholding(self):
        self.click(PayrollWithholdingLocators.add, "Добавить")
        self.click(PayrollWithholdingLocators.withholding, "Удержание")

    def add_statement(self):
        self.click(PayrollWithholdingLocators.addition_input)
        element = self.driver.find_element(By.XPATH, "//li[a='Запросы для б/л']")
        self.move_to_element(element)
        sleep(1)
        self.click(PayrollWithholdingLocators.members_statement)

    def add_pf_request(self):
        self.click(PayrollWithholdingLocators.addition_input)
        element = self.driver.find_element(By.XPATH, "//li[a='Запросы для б/л']")
        self.move_to_element(element)
        sleep(1)
        self.click(PayrollWithholdingLocators.pf_request)

    def add_fss_request(self):
        self.click(PayrollWithholdingLocators.addition_input)
        element = self.driver.find_element(By.XPATH, "//li[a='Запросы для б/л']")
        self.move_to_element(element)
        sleep(1)
        self.click(PayrollWithholdingLocators.fss_request)

    def add_ftn(self):
        self.click(PayrollWithholdingLocators.data_funds)
        self.click(PayrollWithholdingLocators.data_ftn)

    def add_fstn(self):
        self.click(PayrollWithholdingLocators.data_funds)
        self.click(PayrollWithholdingLocators.data_fstn)

    def select_employee(self, value):
        self.search(value)
        self.click_on_employee(value)

    def check_employee(self, value):
        self.search(value)
        self.set_checkbox((By.XPATH, "//input[@type='checkbox']"), True)

    def add_income_certificate(self):
        self.click(PayrollWithholdingLocators.addition_input)
        self.click(PayrollWithholdingLocators.income_certificate)

    def add_reference_previous_place(self):
        self.click(PayrollWithholdingLocators.addition_input)
        self.click(PayrollWithholdingLocators.reference_previous_place)


class PayrollCardPage(BasePage):

    def order(self, value):
        self.set_value(PayrollCardLocators.order, value, "Приказ")

    def date(self, value):
        self.set_date(PayrollCardLocators.date, get_date(value), "Дата")

    def date_from(self, value):
        self.set_date(PayrollCardLocators.date_from, get_date(value), "Период с")

    def date_to(self, value):
        self.set_date(PayrollCardLocators.date_to, value, "Период по")

    def payroll_sum(self, value):
        self.set_value(PayrollCardLocators.payroll_sum, value, "Сумма начисления")

    def average_income_sum(self, value):
        self.set_value(PayrollCardLocators.average_income_sum, value, "Сумма среднего заработка")

    def assessed_date(self, value):
        self.set_date(PayrollCardLocators.assessed_date, value, "Начислено за")

    def awarded_date(self, value):
        self.set_date(PayrollCardLocators.awarded_date, value, "Выплачено в")

    def validity(self, value):
        if value:
            self.set_date(PayrollCardLocators.validity, value, "Срок действия начисления")
        else:
            self.set_date(PayrollCardLocators.validity, '\b\b\b\b\b\b\b\b', "Срок действия начисления")

    def recalculate(self, value):
        self.set_checkbox(PayrollCardLocators.recalculate, value, "Перерасчет")

    def quantify_ban(self, value):
        self.set_checkbox(PayrollCardLocators.quantify_ban, value, "Запретить расчет")

    def count_days(self, value):
        self.set_checkbox(PayrollCardLocators.count_days, value, "Не считать дни")

    def parameters(self, data):
        for i in range(9):
            self.set_value(PayrollCardLocators.parameters[i], data[i], "Заполнение %s параметра" % i)

    def group(self, value):
        self.set_type(PayrollCardLocators.group, value, "Группа учета")

    def financing(self, value):
        self.set_type(PayrollCardLocators.financing, value, "Финансирование")

    def costs(self, value):
        self.set_type(PayrollCardLocators.costs, value, "Затраты")


class WithholdingCardPage(BasePage):

    def order(self, value):
        self.set_value(WithholdingCardLocators.order, value, "Приказ")

    def withholding_sum(self, value):
        self.set_value(WithholdingCardLocators.withholding_sum, value, "Сумма удержания")

    def validity(self, value):
        if value:
            self.set_date(WithholdingCardLocators.validity, value, "Срок действия удержания")
        else:
            self.clear_date_field(WithholdingCardLocators.validity)

    def assessed_date(self, value):
        self.set_date(WithholdingCardLocators.assessed_date, value, "Начислено за")

    def awarded_date(self, value):
        self.set_date(WithholdingCardLocators.awarded_date, value, "Рассчитано в")

    def quantify_ban(self, value):
        self.set_checkbox(WithholdingCardLocators.quantify_ban, value, "Запретить расчет")

    def recalculation(self, value):
        self.set_checkbox(WithholdingCardLocators.recalculation, value, "Перерасчет")

    def parameters(self, data):
        for i in range(9):
            self.set_value(WithholdingCardLocators.parameters[i], data[i], "Заполнение %s параметра" % i)

    def payment_accruals(self, value):
        self.set_value(WithholdingCardLocators.payment_accruals, value, "Межвыплата по начислениям")

    def executive_sheet(self, value):
        self.set_type(WithholdingCardLocators.executive_sheet, value, "Исполнительный лист")


class StatementCardPage(BasePage):

    def full_name(self, value):
        self.set_value(StatementCardLocators.full_name, value, "От сотрудника")

    def period_from(self, value):
        self.set_date(StatementCardLocators.period_from, value, "Период работы с")

    def period_to(self, value):
        self.set_date(StatementCardLocators.period_to, value, "Период работы по")

    def insurer(self, value):
        self.set_value(StatementCardLocators.insurer, value, "У страхователя")

    def reason(self, value):
        self.set_value(StatementCardLocators.reason, value, "Причина невозможности получить справку")

    def payment(self, value):
        self.set_select(value, "Для оплаты")

    def statement_date(self, value):
        self.set_date(StatementCardLocators.statement_date, get_date(value), "Дата заявления")


class PFRequestCardPage(BasePage):

    def unit(self, value):
        self.wait_for_loading()
        self.set_value(PFRequestCardLocators.unit, value, "В территориальный орган ПФР")

    def additional(self, value):
        self.set_value(PFRequestCardLocators.additional, value, "Дополнительные сведения о страховке")

    def full_name(self, value):
        self.set_value(PFRequestCardLocators.full_name, value, "По заявлению сотрудника")

    def year_first(self, value):
        self.set_value(PFRequestCardLocators.year_first, value, "Годы работы первое поле")

    def year_second(self, value):
        self.set_value(PFRequestCardLocators.year_second, value, "Годы работы второе поле")

    def year_third(self, value):
        self.set_value(PFRequestCardLocators.year_third, value, "Годы работы третье поле")

    def insurer(self, value):
        self.set_value(PFRequestCardLocators.insurer, value, "У страхователя")

    def reason(self, value):
        self.set_value(PFRequestCardLocators.reason, value, "Причина невозможности получить справку")

    def payment(self, value):
        self.set_select(value, "Для оплаты")

    def request_date(self, value):
        self.set_date(PFRequestCardLocators.request_date, get_date(value), "Дата запроса")

    def request_number(self, value):
        self.set_value(PFRequestCardLocators.request_number, value, "Номер запроса")

    def manager(self, value):
        self.set_select(value, "Руководитель")


class FSSRequestCardPage(BasePage):

    def unit(self, value):
        self.set_value(FSSRequestCardLocators.unit, value, "В территориальный орган ФСС")

    def full_name(self, value):
        self.set_value(FSSRequestCardLocators.full_name, value, "Для оплаты сотруднику")

    def type(self, value):
        self.set_select(value, "Вид пособия")

    def first_employer(self, value):
        self.set_value(FSSRequestCardLocators.first_employer, value, "Первый работодатель")

    def first_itn(self, value):
        self.set_value(FSSRequestCardLocators.first_itn, value, "ИНН первого работодателя")

    def first_unit(self, value):
        self.set_value(FSSRequestCardLocators.first_unit, value, "Терриориальный орган первого работодателя")

    def first_kpp(self, value):
        self.set_value(FSSRequestCardLocators.first_kpp, value, "КПП первого работодателя")

    def first_registration_number(self, value):
        self.set_value(FSSRequestCardLocators.first_registration_number, value,
                       "Регистрационный номер первого работодателя")

    def first_additional_code(self, value):
        self.set_value(FSSRequestCardLocators.first_additional_code, value, "Дополнительный код первого работодателя")

    def first_code(self, value):
        self.set_value(FSSRequestCardLocators.first_code, value, "Код подчиненного первого работодателя")

    def first_period_from(self, value):
        self.set_date(FSSRequestCardLocators.first_period_from, value, "Период работы с у первого работодателя")

    def first_period_to(self, value):
        self.set_date(FSSRequestCardLocators.first_period_to, value, "Период работы по у первого работодателя")

    def second_employer(self, value):
        self.set_value(FSSRequestCardLocators.second_employer, value, "Второй работодатель")

    def second_itn(self, value):
        self.set_value(FSSRequestCardLocators.second_itn, value, "ИНН второго работодателя")

    def second_unit(self, value):
        self.set_value(FSSRequestCardLocators.second_unit, value, "Территориальный орган второго работодателя")

    def second_kpp(self, value):
        self.set_value(FSSRequestCardLocators.second_kpp, value, "КПП второго работодателя")

    def second_registration_number(self, value):
        self.set_value(FSSRequestCardLocators.second_registration_number, value,
                       "Регистрационный номер второго работодателя")

    def second_additional_code(self, value):
        self.set_value(FSSRequestCardLocators.second_additional_code, value, "Дополнительный код второго работодателя")

    def second_code(self, value):
        self.set_value(FSSRequestCardLocators.second_code, value, "Код подчиненного второго работодателя")

    def second_period_from(self, value):
        self.set_date(FSSRequestCardLocators.second_period_from, value, "Период работы с у второго работодателя")

    def second_period_to(self, value):
        self.set_date(FSSRequestCardLocators.second_period_to, value, "Период работы по у второго работодателя")

    def third_employer(self, value):
        self.set_value(FSSRequestCardLocators.third_employer, value, "Третий работодатель")

    def third_itn(self, value):
        self.set_value(FSSRequestCardLocators.third_itn, value, "ИНН третьего работодателя")

    def third_unit(self, value):
        self.set_value(FSSRequestCardLocators.third_unit, value, "Территориальный орган третьего работодателя")

    def third_kpp(self, value):
        self.set_value(FSSRequestCardLocators.third_kpp, value, "КПП третьего работодателя")

    def third_registration_number(self, value):
        self.set_value(FSSRequestCardLocators.third_registration_number, value,
                       "Регистрационный номер третьего работодателя")

    def third_additional_code(self, value):
        self.set_value(FSSRequestCardLocators.third_additional_code, value, "Дополнительный код третьего работодателя")

    def third_code(self, value):
        self.set_value(FSSRequestCardLocators.third_code, value, "Код подчиненного третьего работодателя")

    def third_period_from(self, value):
        self.set_date(FSSRequestCardLocators.third_period_from, value, "Период работы с у третьего работодателя")

    def third_period_to(self, value):
        self.set_date(FSSRequestCardLocators.third_period_to, value, "Период работы по у третьего работодателя")

    def request_date(self, value):
        self.set_date(FSSRequestCardLocators.request_date, get_date(value), "Дата запроса")


class FTNPage(BasePage):

    def add(self):
        self.click_by_name("Добавить")


class FTNCardPage(BasePage):

    def base(self, value):
        self.set_value(FTNCardLocators.base, value, "Облагаемая база")

    def discount(self, value):
        self.set_value(FTNCardLocators.discount, value, "Скидка")

    def privilege(self, value):
        self.set_value(FTNCardLocators.privilege, value, "Льготы")

    def material_assistance(self, value):
        self.set_value(FTNCardLocators.material_assistance, value, "Материальная помощь")

    def amount(self, value):
        self.set_value(FTNCardLocators.amount, value, "Количество детей")


class FSTNPage(BasePage):

    def add(self):
        self.click_by_name("Добавить")


class FSTNCardPage(BasePage):

    def fund(self, value):
        self.set_type(FSTNCardLocators.fund, value, "Фонд")

    def base(self, value):
        self.set_value(FSTNCardLocators.base, value, "Облагаемая база")

    def disabled_base(self, value):
        self.set_value(FSTNCardLocators.disabled_base, value, "Облагаемая база инвалида")

    def discount(self, value):
        self.set_value(FSTNCardLocators.discount, value, "Скидка")

    def deductions(self, value):
        self.set_value(FSTNCardLocators.deductions, value, "Отчисления")

    def disabled_deductions(self, value):
        self.set_value(FSTNCardLocators.disabled_deductions, value, "Отчисления инвалиду")

    def material_assistance(self, value):
        self.set_value(FSTNCardLocators.material_assistance, value, "Материальная помощь")

    def amount(self, value):
        self.set_value(FSTNCardLocators.amount, value, "Количество детей")


class IncomeCertificatePage(BasePage):

    def incomes(self):
        self.click_by_name("Доходы")

    def deductions(self):
        self.click_by_name("Вычеты")

    def date(self, value):
        self.set_date_cut(IncomeCertificateLocators.date, value, "Месяц и год выхода")

    def tax_sum(self, value):
        self.set_value(IncomeCertificateLocators.tax_sum, value, "Сумма налога")

    def income_sum(self, value):
        self.set_value(IncomeCertificateLocators.income_sum, value, "Сумма")

    def income_type(self, value):
        self.set_type(IncomeCertificateLocators.income_type, value, "Тип дохода")

    def deduction_sum(self, value):
        self.set_value(IncomeCertificateLocators.deduction_sum, value, "Сумма")

    def deduction_type(self, value):
        self.set_type(IncomeCertificateLocators.deduction_type, value, "Тип вычета")

    def childs_amount(self, value):
        self.set_value(IncomeCertificateLocators.childs_amount, value, "Количество детей")

    def submit(self):
        self.click_by_name("Сохранить")

    def submit2(self):
        self.click(IncomeCertificateLocators.submit2, "Сохранить")


class ReferencePreviousPlacePage(BasePage):

    def issue_date(self, value):
        self.set_date(ReferencePreviousPlaceLocators.issue_date, value, "Дата выдачи")

    def reference_number(self, value):
        self.set_value(ReferencePreviousPlaceLocators.reference_number, value, "Номер справки")

    def insurer(self, value):
        self.set_value(ReferencePreviousPlaceLocators.insurer, value, "Страхователь")

    def periods_period_from(self, value):
        self.set_date(ReferencePreviousPlaceLocators.periods_period_from, value, "Период с")

    def periods_period_to(self, value):
        self.set_date(ReferencePreviousPlaceLocators.periods_period_to, value, "Период по")

    def periods_include(self, value):
        self.set_checkbox(ReferencePreviousPlaceLocators.periods_include, value, "Включить")

    def salary_year(self, value):
        self.set_value(ReferencePreviousPlaceLocators.salary_year, value, "Год")

    def salary_sum(self, value):
        self.set_value(ReferencePreviousPlaceLocators.salary_sum, value, "Сумма заработка")

    def salary_include(self, value):
        self.set_checkbox(ReferencePreviousPlaceLocators.salary_include, value, "Включить")

    def days_year(self, value):
        self.set_value(ReferencePreviousPlaceLocators.days_year, value, "Год")

    def days_period_from(self, value):
        self.set_date(ReferencePreviousPlaceLocators.days_period_from, value, "Исключаемый период с")

    def days_period_to(self, value):
        self.click(ReferencePreviousPlaceLocators.days_period_to)
        self.wait_for_loading()
        self.set_date(ReferencePreviousPlaceLocators.days_period_to, value, "Исключаемый период по")

    def days_amount(self, value):
        self.click(ReferencePreviousPlaceLocators.days_amount)
        self.wait_for_loading()
        self.set_value(ReferencePreviousPlaceLocators.days_amount, value, "Исключаемые дни")

    def days_name(self, value):
        self.set_select(value, "Наименование периода")

    def days_include(self, value):
        self.set_checkbox(ReferencePreviousPlaceLocators.days_include, value, "Включить")

