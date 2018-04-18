from pages import *
from setup import *
import pytest


class TestSuite:
    driver = webdriver.Chrome("driver\\chromedriver.exe")

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        #  cls.driver = webdriver.Chrome("C:\Python34\Scripts\chromedriver.exe")
        #  cls.driver =webdriver.Ie("C:\Python34\Scripts\IEDriverServer.exe")
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    # def setup(self):
    #     MainPage(self.driver).open()

    @pytest.mark.parametrize("n", ["Администратор"])
    def test_login(self, n):
        """
        Проверяется возможность авторизации на портале.
        """
        data = get_account_by_name(load_data("accounts"), n)

        #
        p = LoginPage(self.driver)
        self.driver.get(Links.main_page)
        p.username(data["username"])
        p.password(data["password"])
        p.lot(data["lot"])
        p.submit()
        assert "Учет заработной платы" in self.driver.page_source

    @pytest.mark.parametrize("n", ["Артюшин", "Коновалов", "Зотова", "Парамонова"])
    def test_new_employee(self, n):
        """
        Проверяется возможность создание нового сотрудника. Заполняются все поля следующих вкладок: Документы,
        Адреса, Данные ПФР, Данные ФНС, История ФИО, Прочее.
        """
        data = get_employee_by_name(load_data("employees"), n)

        #
        p = Menu(self.driver)
        p.open()
        p.catalogs()
        p.employees()

        #
        p = EmployeesPage(self.driver)
        p.add()

        #
        # p = PersonalAccountPage(self.driver)
        # p.open()

        #
        p = EmployeeCardPage(self.driver)
        # p.open()
        p.last_name(data["lastName"])
        p.first_name(data["firstName"])
        p.middle_name(data["middleName"])
        p.gender(data["gender"])
        p.birthday(data["birthday"])
        p.submit()

        #
        p = DocumentsPage(self.driver)
        p.open()
        p.document_type(data["documents"]["documentType"])
        p.serial_number(data["documents"]["serialFirst"],
                        data["documents"]["serialSecond"],
                        data["documents"]["serialThird"])
        p.department_code(data["documents"]["departmentCode"])
        p.issue_date(data["documents"]["issueDate"])
        p.issued_by(data["documents"]["issuedBy"])

        #
        p = AddressesPage(self.driver)
        p.open()
        p.index(data["addresses"]["index"])
        p.region(data["addresses"]["region"])
        p.area(data["addresses"]["area"])
        p.area_type(data["addresses"]["areaType"])
        p.city(data["addresses"]["city"])
        p.city_type(data["addresses"]["cityType"])
        p.locality(data["addresses"]["locality"])
        p.locality_type(data["addresses"]["localityType"])
        p.street(data["addresses"]["street"])
        p.street_type(data["addresses"]["streetType"])
        p.building(data["addresses"]["building"])
        p.block(data["addresses"]["block"])
        p.apartment(data["addresses"]["apartment"])
        p.use(data["addresses"]["use"])
        p.actual_address(data["addresses"]["actualAddress"])

        #
        p = PFRPage(self.driver)
        p.open()
        p.registration_number(data["pfr"]["registrationNumber"])
        p.category(data["pfr"]["category"])
        p.locality_type(data["pfr"]["localityType"])
        p.retirement_date(data["pfr"]["retirementDate"])
        p.esn(data["pfr"]["esn"])
        p.last_name(data["pfr"]["lastName"])
        p.first_name(data["pfr"]["firstName"])
        p.middle_name(data["pfr"]["middleName"])
        p.nationality(data["pfr"]["nationality"])
        p.exclude(data["pfr"]["exclude"])
        p.country(data["pfr"]["country"])
        p.region(data["pfr"]["region"])
        p.area(data["pfr"]["area"])
        p.city(data["pfr"]["city"])

        #
        p = FNSPage(self.driver)
        p.open()
        p.itn(data["fns"]["itn"])
        p.exclude(data["fns"]["exclude"])
        p.resident(data["fns"]["resident"])
        p.nationality(data["fns"]["nationality"])

        #
        p = FullNamePage(self.driver)
        p.open()

        #
        p = OtherPage(self.driver)
        p.open()
        p.requisites(data["other"]["requisites"])
        p.phone_number(data["other"]["phoneNumber"])
        p.email(data["other"]["email"])
        p.crimea(data["other"]["crimea"])

        EmployeeCardPage(self.driver).save()

    @pytest.mark.parametrize("n", ["Артюшин", "Коновалов", "Зотова", "Парамонова"])
    def test_add_personal_account(self, n):
        """
        Проверяется возможность добавления лицевого счета существующему сотруднику. Заполняются все поля из следующих
        вкладок: Сведения о лицевом счете, Сведения для расчета, Льготы на сотрудника.
        """
        data = get_employee_by_name(load_data("employees"), n)
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.catalogs()
        p.employees()
        EmployeesPage(self.driver).select_employee(n)
        #
        p = PersonalAccountPage(self.driver)
        # p.open()
        p.add()

        #
        p = AccountInfoPage(self.driver)
        # p.open()
        p.personnel_number(data["personalAccount"]["accountInfo"]["personnelNumber"])
        p.receipt_date(data["personalAccount"]["accountInfo"]["receiptDate"])
        p.order_number(data["personalAccount"]["accountInfo"]["orderNumber"])
        p.salary_amount(data["personalAccount"]["accountInfo"]["salaryAmount"])
        p.working_hours(data["personalAccount"]["accountInfo"]["workingHours"])
        p.change_date(data["personalAccount"]["accountInfo"]["changeDate"])
        p.payment_category(data["personalAccount"]["accountInfo"]["paymentCategory"])
        p.payment_category_by(data["personalAccount"]["accountInfo"]["employeeCategoryBy"])
        p.time_category(data["personalAccount"]["accountInfo"]["timeCategory"])
        p.status_on(data["personalAccount"]["accountInfo"]["statusOn"])
        p.status_off(data["personalAccount"]["accountInfo"]["statusOff"])
        p.ets(data["personalAccount"]["accountInfo"]["ets"])
        p.subdivision(data["personalAccount"]["accountInfo"]["subdivision"])
        p.position(data["personalAccount"]["accountInfo"]["position"])
        p.experience(data["personalAccount"]["accountInfo"]["experience"])
        p.last_payroll(data["personalAccount"]["accountInfo"]["lastPayroll"])
        p.dismissal_date(data["personalAccount"]["accountInfo"]["dismissalDate"])
        p.fired(data["personalAccount"]["accountInfo"]["fired"])
        p.dismissal_number(data["personalAccount"]["accountInfo"]["dismissalNumber"])
        sleep(5)
        p.employee_category(data["personalAccount"]["accountInfo"]["employeeCategory"])
        sleep(5)
        p.class_rank(data["personalAccount"]["accountInfo"]["classRank"])
        p.union_member(data["personalAccount"]["accountInfo"]["unionMember"])
        p.member_from(data["personalAccount"]["accountInfo"]["memberFrom"])
        p.member_to(data["personalAccount"]["accountInfo"]["memberTo"])
        p.employee_number(data["personalAccount"]["accountInfo"]["employeeNumber"])

        #
        p = CalcInfoPage(self.driver)
        p.open()
        p.holiday_payment(data["personalAccount"]["calcInfo"]["holidayPayment"])
        p.holiday_period_from(data["personalAccount"]["calcInfo"]["holidayPeriodFrom"])
        p.holiday_period_to(data["personalAccount"]["calcInfo"]["holidayPeriodTo"])
        p.note(data["personalAccount"]["calcInfo"]["note"])
        p.sick_days_percent(data["personalAccount"]["calcInfo"]["sickDaysPercent"])
        p.average_daily_earnings(data["personalAccount"]["calcInfo"]["averageDailyEarnings"])
        p.privileges_type(data["personalAccount"]["calcInfo"]["privilegesType"])
        p.coefficient(data["personalAccount"]["calcInfo"]["coefficient"])
        p.state_employee(data["personalAccount"]["calcInfo"]["stateEmployee"])
        p.main_work(data["personalAccount"]["calcInfo"]["mainWork"])
        p.resident(data["personalAccount"]["calcInfo"]["resident"])
        p.pluralist(data["personalAccount"]["calcInfo"]["pluralist"])
        p.chaes_member(data["personalAccount"]["calcInfo"]["chaesMember"])
        p.chaes_number(data["personalAccount"]["calcInfo"]["chaesNumber"])
        p.salary_without_rounding(data["personalAccount"]["calcInfo"]["salaryWithoutRounding"])
        p.income_tax(data["personalAccount"]["calcInfo"]["incomeTax"])
        p.prepaid_expense(data["personalAccount"]["calcInfo"]["prepaidExpense"])
        p.region(data["personalAccount"]["calcInfo"]["region"])
        p.alimony(data["personalAccount"]["calcInfo"]["alimony"])
        p.stb_card(data["personalAccount"]["calcInfo"]["stbCard"])
        p.payment_method(data["personalAccount"]["calcInfo"]["paymentMethod"])
        p.card_number(data["personalAccount"]["calcInfo"]["cardNumber"])
        p.full_name(data["personalAccount"]["calcInfo"]["fullName"])
        p.validity(data["personalAccount"]["calcInfo"]["validity"])
        p.bank_list(data["personalAccount"]["calcInfo"]["bankList"])
        p.key(data["personalAccount"]["calcInfo"]["key"])

        #
        p = EmployeePrivilegesPage(self.driver)
        p.open()
        p.add()
        p.date_start(data["personalAccount"]["employeePrivileges"]["dateStart"])
        p.date_end(data["personalAccount"]["employeePrivileges"]["dateEnd"])
        if data["personalAccount"]["employeePrivileges"]["childPrivilege"]:
            p.child_privilege(data["personalAccount"]["employeePrivileges"]["childPrivilege"])
            p.renouncement(data["personalAccount"]["employeePrivileges"]["renouncement"])
            p.child_number(data["personalAccount"]["employeePrivileges"]["childNumber"])
            p.statement_number(data["personalAccount"]["employeePrivileges"]["statementNumber"])
            p.single_parent(data["personalAccount"]["employeePrivileges"]["singleParent"])
            p.birthday(data["personalAccount"]["employeePrivileges"]["birthday"])
            p.statement_date(data["personalAccount"]["employeePrivileges"]["statementDate"])
        if data["personalAccount"]["employeePrivileges"]["disabled"]:
            p.disabled(data["personalAccount"]["employeePrivileges"]["disabled"])
            p.tutor(data["personalAccount"]["employeePrivileges"]["tutor"])
        p.tax_deduction(data["personalAccount"]["employeePrivileges"]["taxDeduction"])
        p.professional_deduction(data["personalAccount"]["employeePrivileges"]["professionalDeduction"])
        p.social_deduction(data["personalAccount"]["employeePrivileges"]["socialDeduction"])
        p.note(data["personalAccount"]["employeePrivileges"]["note"])
        p.privileges_amount(data["personalAccount"]["employeePrivileges"]["privilegesAmount"])
        p.deduction_code(data["personalAccount"]["employeePrivileges"]["deductionCode"])
        p.deduction_sum(data["personalAccount"]["employeePrivileges"]["deductionSum"])
        p.imns(data["personalAccount"]["employeePrivileges"]["imns"])
        p.notification_number(data["personalAccount"]["employeePrivileges"]["notificationNumber"])
        p.notification_date(data["personalAccount"]["employeePrivileges"]["notificationDate"])
        p.submit()
        EmployeeCardPage(self.driver).submit2()
        #
        EmployeeCardPage(self.driver).tariff_salary(data["personalAccount"]["tariffSalary"])
        EmployeeCardPage(self.driver).submit2()
        sleep(3)
        EmployeeCardPage(self.driver).submit()

    @pytest.mark.parametrize("n", ["Коновалов"])
    def test_add_members_statement(self, n):
        """
         Проверяется возможность добавления начислений/удержаний существующему сотруднику.
        """
        data = get_employee_by_name(load_data("employees"), n)

        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.subdivision_structure()

        PayrollWithholdingPage(self.driver).add_statement()

        #
        for statement in data["memberStatements"]:
            p = StatementCardPage(self.driver)
            p.full_name(statement["fullName"])
            p.period_from(statement["periodFrom"])
            p.period_to(statement["periodTo"])
            p.insurer(statement["insurer"])
            p.reason(statement["reason"])
            p.payment(statement["payment"])
            p.statement_date(statement["statementDate"])
            p.click_by_name("Сохранить")

    @pytest.mark.parametrize("n", ["Коновалов"])
    def test_add_pf_request(self, n):
        """
         Проверяется возможность запроса для б/л в ПФ.
        """
        data = get_employee_by_name(load_data("employees"), n)

        print(data)
        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.subdivision_structure()

        PayrollWithholdingPage(self.driver).add_pf_request()

        #
        for request in data["pfRequests"]:
            p = PFRequestCardPage(self.driver)
            sleep(20)
            p.unit(request["unit"])
            p.additional(request["additional"])
            p.full_name(request["fullName"])
            p.year_first(request["yearFirst"])
            p.year_second(request["yearSecond"])
            p.year_third(request["yearThird"])
            p.insurer(request["insurer"])
            p.reason(request["reason"])
            p.payment(request["payment"])
            p.request_date(request["requestDate"])
            p.request_number(request["requestNumber"])
            p.manager(request["manager"])
            p.click_by_name("Сохранить")

    @pytest.mark.parametrize("n", ["Коновалов"])
    def test_add_fss_request(self, n):
        """
         Проверяется возможность добавления запроса для б/л в ФСС.
        """
        data = get_employee_by_name(load_data("employees"), n)

        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.subdivision_structure()

        PayrollWithholdingPage(self.driver).add_fss_request()

        #
        for request in data["fssRequests"]:
            p = FSSRequestCardPage(self.driver)
            p.unit(request["unit"])
            p.full_name(request["fullName"])
            p.type(request["type"])
            p.first_employer(request["firstEmployer"])
            p.first_itn(request["firstItn"])
            p.first_unit(request["firstUnit"])
            p.first_kpp(request["firstKpp"])
            p.first_registration_number(request["firstRegistrationNumber"])
            p.first_additional_code(request["firstAdditionalCode"])
            p.first_code(request["firstCode"])
            p.first_period_from(request["firstPeriodFrom"])
            p.first_period_to(request["firstPeriodTo"])
            p.second_employer(request["secondEmployer"])
            p.second_itn(request["secondItn"])
            p.second_unit(request["secondUnit"])
            p.second_kpp(request["secondKpp"])
            p.second_registration_number(request["secondRegistrationNumber"])
            p.second_additional_code(request["secondAdditionalCode"])
            p.second_code(request["secondCode"])
            p.second_period_from(request["secondPeriodFrom"])
            p.second_period_to(request["secondPeriodTo"])
            p.third_employer(request["thirdEmployer"])
            p.third_itn(request["thirdItn"])
            p.third_unit(request["thirdUnit"])
            p.third_kpp(request["thirdKpp"])
            p.third_registration_number(request["thirdRegistrationNumber"])
            p.third_additional_code(request["thirdAdditionalCode"])
            p.third_code(request["thirdCode"])
            p.third_period_from(request["thirdPeriodFrom"])
            p.third_period_to(request["thirdPeriodTo"])
            p.request_date(request["requestDate"])
            p.click_by_name("Сохранить")

    @pytest.mark.parametrize("n", ["Коновалов"])
    def test_add_extra_budgetary_references(self, n):
        """
         Проверяется возможность добавления справки по внебюджетным фондам из обособленного подразделения
         существующему сотруднику.
        """
        data = get_employee_by_name(load_data("employees"), n)

        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.subdivision_structure()

        #
        p = PayrollWithholdingPage(self.driver)
        p.check_employee(n)
        p.add_ftn()

        #
        for reference in data["ftn"]:
            sleep(10)
            FTNPage(self.driver).add()
            p = FTNCardPage(self.driver)
            p.base(reference["base"])
            p.discount(reference["discount"])
            p.privilege(reference["privilege"])
            p.material_assistance(reference["materialAssistance"])
            p.amount(reference["amount"])
            p.click_by_name("Сохранить")

        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.subdivision_structure()

        #
        p = PayrollWithholdingPage(self.driver)
        p.check_employee(n)
        p.add_fstn()

        #
        for reference in data["fstn"]:
            sleep(5)
            FSTNPage(self.driver).add()
            sleep(5)
            p = FSTNCardPage(self.driver)
            p.fund(reference["fund"])
            p.base(reference["base"])
            p.disabled_base(reference["disabledBase"])
            p.discount(reference["discount"])
            p.deductions(reference["deductions"])
            p.disabled_deductions(reference["disabledDeductions"])
            p.material_assistance(reference["materialAssistance"])
            p.amount(reference["amount"])
            p.click_by_name("Сохранить")

    @pytest.mark.parametrize("n", ["Парамонова"])
    def test_add_disabled_reference(self, n):
        """
         Проверяется возможность добавления справки об инвалидности.
        """
        data = get_employee_by_name(load_data("employees"), n)

        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.disabled()

        #
        DisabledPage(self.driver).add()
        p = DisabledCardPage(self.driver)

        #
        for reference in data["disabledReferences"]:
            p.full_name(reference["fullName"])
            p.reference(reference["reference"])
            p.reference_number(reference["referenceNumber"])
            p.date(reference["date"])
            p.group(reference["group"])
            p.validity(reference["validity"])
            p.click_by_name("Сохранить")

    @pytest.mark.parametrize("n", ["Артюшин", "Коновалов", "Зотова", "Парамонова"])
    def test_add_payroll_and_withholding(self, n):
        """
         Проверяется возможность добавления начислений/удержаний существующему сотруднику.
        """
        data = get_employee_by_name(load_data("employees"), n)

        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.subdivision_structure()
        parent = PayrollWithholdingPage(self.driver)
        parent.select_employee(n)

        #
        flag = True
        for i in data["payrolls"]:
            if i["lastMonth"] and flag:
                flag = False
                parent.prev_month()
            if not i["lastMonth"] and not flag:
                flag = True
                parent.next_month()
            #
            parent.add_payroll()
            parent.set_type_alt(i["payroll"], "Справочник начислений")
            child = PayrollCardPage(self.driver)
            child.order(i["order"])
            child.date(i["date"])
            child.date_from(i["dateFrom"])
            child.date_to(i["dateTo"])
            child.payroll_sum(i["payrollSum"])
            child.average_income_sum(i["averageIncomeSum"])
            child.assessed_date(i["assessedDate"])
            child.awarded_date(i["awardedDate"])
            child.validity(i["validity"])
            child.recalculate(i["recalculate"])
            child.quantify_ban(i["quantifyBan"])
            child.count_days(i["countDays"])
            child.parameters(i["parameters"])
            child.group(i["group"])
            child.financing(i["financing"])
            child.costs(i["costs"])
            child.click_by_name("Сохранить")
            sleep(1)
            child.click_by_name("Да")
            sleep(10)

        #
        parent = PayrollWithholdingPage(self.driver)
        for i in data["withholdings"]:
            if i["lastMonth"] and flag:
                flag = False
                parent.prev_month()
            if not i["lastMonth"] and not flag:
                flag = True
                parent.next_month()

            #
            parent.add_withholding()
            parent.set_type_alt(i["withholding"], "Справочник удержаний")
            child = WithholdingCardPage(self.driver)
            child.order(i["order"])
            child.withholding_sum(i["withholdingSum"])
            child.validity(i["validity"])
            child.assessed_date(i["assessedDate"])
            child.awarded_date(i["awardedDate"])
            child.quantify_ban(i["quantifyBan"])
            child.recalculation(i["recalculation"])
            child.parameters(i["parameters"])
            child.payment_accruals(i["paymentAccruals"])
            child.executive_sheet(i["executiveSheet"])
            child.click_by_name("Сохранить", 2)

        sleep(5)

    @pytest.mark.parametrize("n", ["Артюшин", "Коновалов", "Зотова", "Парамонова"])
    def test_add_employee_earning_certificate(self, n):
        """
         Проверяется возможность добавления справки 2НДФЛ.
        """
        data = get_employee_by_name(load_data("employees"), n)

        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.subdivision_structure()

        #
        p = PayrollWithholdingPage(self.driver)
        p.check_employee(n)
        p.add_income_certificate()

        #
        p = IncomeCertificatePage(self.driver)
        p.click_by_name("Добавить")
        p.date(data["incomeTaxes"]["date"])
        sleep(5)
        p.tax_sum(data["incomeTaxes"]["taxSum"])
        p.submit()

        #
        p.incomes()
        for i in data["incomeTaxes"]["incomes"]:
            p.click_by_name("Добавить")
            p.income_sum(i["sum"])
            p.income_type(i["type"])
            p.submit()
        p.click_by_name("Закрыть")

        #
        p.deductions()
        for i in data["incomeTaxes"]["deductions"]:
            p.click_by_name("Добавить", 2)
            p.deduction_sum(i["sum"])
            p.deduction_type(i["type"])
            p.childs_amount(i["childsAmount"])
            p.submit()
            sleep(5)
        p.click_by_name("Закрыть", 2)
        p.click_by_name("Закрыть")
        # p.submit()

    @pytest.mark.parametrize("n", ["Артюшин", "Коновалов", "Зотова", "Парамонова"])
    def test_reference_from_previous_place_of_work(self, n):
        """
         Проверяется возможность добавления справки с предыдущего места работы.
        """
        data = get_employee_by_name(load_data("employees"), n)

        #
        # MainPage(self.driver).open()
        p = Menu(self.driver)
        p.open()
        p.documents()
        p.subdivision_structure()

        #
        p = PayrollWithholdingPage(self.driver)
        p.check_employee(n)
        p.add_reference_previous_place()
        p.click_by_name("Да", 2)

        #
        for ref in data["referencePreviousPlace"]:
            p = ReferencePreviousPlacePage(self.driver)
            p.click_by_name("Добавить")
            p.issue_date(ref["issueDate"])
            p.reference_number(ref["referenceNumber"])
            p.insurer(ref["insurer"])
            p.click_by_name("Сохранить")

            #
            p.click_by_name("Периоды работы")
            for i in ref["periods"]:
                p.click_by_name("Добавить", 2)
                p.periods_period_from(i["periodFrom"])
                p.periods_period_to(i["periodTo"])
                p.periods_include(i["include"])
                p.click_by_name("Сохранить")
            p.click_by_name("Закрыть", 2)

            #
            p.click_by_name("Сумма ЗП")
            for i in ref["salary"]:
                p.click_by_name("Добавить", 2)
                p.salary_year(i["year"])
                p.salary_sum(i["sum"])
                p.salary_include(i["include"])
                p.click_by_name("Сохранить")
            p.click_by_name("Закрыть", 2)

            #
            p.click_by_name("Иcключаемые дни")
            for i in ref["days"]:
                p.click_by_name("Добавить", 2)
                p.days_year(i["year"])
                p.days_period_from(i["periodFrom"])
                p.days_period_to(i["periodTo"])
                p.days_amount(i["amount"])
                p.days_name(i["name"])
                p.days_include(i["include"])
                sleep(3)
                p.click_by_name("Сохранить")
            p.click_by_name("Закрыть", 2)
        p.click_by_name("Закрыть")

    def test_logout(self):
        """
        Тест проверяет возможность деавторизации на портале.
        """
        MainPage(self.driver).logout()
        assert "Идентификация пользователя" in self.driver.page_source

