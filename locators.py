from selenium.webdriver.common.by import By


class LoginLocators(object):

    username = (By.ID, "UserName")
    password = (By.ID, "Password")
    lot = (By.XPATH, "//a[normalize-space(text())='Выберите']")
    submit = (By.XPATH, "//button[@type='submit']")


class MainLocators(object):

    logout = (By.XPATH, "//a[@href='/Account/Logoff']")


class MenuLocators(object):
    """
    menu_icon = (By.XPATH, "//button[@class='left-menu-toggle']")
    catalogs = (By.XPATH, "//span[normalize-space(text())='Справочники']")
    employees = (By.XPATH, "//span[normalize-space(text())='Сотрудники']")
    documents = (By.XPATH, "//span[normalize-space(text())='Документы']")
    disabled = (By.XPATH, "//span[normalize-space(text())='Инвалиды']")
    subdivision_structure = (By.XPATH, "//span[normalize-space(text())='Структура подразделений']")
    """
    menu_icon = (By.XPATH, "//button[@class='left-menu-toggle']")
    catalogs = (By.XPATH, "//span[@class='ng-binding'][.='Справочники']")
    employees = (By.XPATH, "//span[@class='ng-binding'][.='Сотрудники']")
    documents = (By.XPATH, "//span[@class='ng-binding'][.='Документы']")
    disabled = (By.XPATH, "//span[@class='ng-binding'][.='Инвалиды']")
    subdivision_structure = (By.XPATH, "//span[@class='ng-binding'][.='Структура подразделений']")

class EmployeesLocators(object):

    add = (By.XPATH, "//button[normalize-space(text())='Добавить']")


class EmployeeCardLocators(object):

    edit_button = (By.XPATH, "//button[normalize-space(text())='Личные данные']")
    last_name = (By.ID, "24afcfb0-dfa7-4c97-8c59-0ec905f7854d")
    first_name = (By.ID, "b9fd1a97-1d29-4669-89cd-0991e04bfb88")
    middle_name = (By.ID, "27048dc7-fc23-40f0-be77-62621d03ce44")
    gender = ()
    birthday = (By.ID, "41e0b8cb-1e5b-4fda-a032-dfa4c87fc011")

    submit3 = (By.XPATH, "(//div[@aria-labelledby='ui-dialog-title-4']//button[.='Сохранить'])")
    submit2 = (By.XPATH, "(//button[.='Сохранить'])[2]")
    submit = (By.XPATH, "(//button[.='Сохранить'])")
    save = (By.XPATH, "//button[.='Сохранить']")
    tariff_salary = (By.ID, "9dd40848-e320-40dc-ae70-c1250e9148a7")
    dialog_save = (By.XPATH, "(//button[@data-button-id='e8cb4670-9b38-465a-a7ad-c483e5360623'])[2]")


class StatementCardLocators(object):

    full_name = (By.ID, "7f9a431a-be64-4d86-8892-a12b92427744")
    period_from = (By.ID, "6606648c-37c2-44ae-a931-4ed7589e0497")
    period_to = (By.ID, "1ff2f2e4-68ed-4e08-95f3-568bf716d5bd")
    insurer = (By.ID, "c92c1539-6b13-49fa-bd71-09a5a97f1fa6")
    reason = (By.ID, "9ffc8098-e386-4c17-95b8-b44ed5914606")
    payment = ()
    statement_date = (By.ID, "d77522f7-98c0-4924-b0ab-22a3be24c38d")


class PFRequestCardLocators(object):

    unit = (By.ID, "e4b91b35-bb1d-4a77-9fbe-0569409903d0")
    additional = (By.ID, "092a5990-03f6-4478-b85c-62b5718499ea")
    full_name = (By.ID, "4d2b5714-eb9c-431f-becd-014e5d611ba0")
    year_first = (By.ID, "dd44244d-ca02-476f-b703-49c853149fc5")
    year_second = (By.ID, "3c0e53f5-6fdd-47e8-9682-a379da1864cb")
    year_third = (By.ID, "56baf6c0-5f64-4f1f-86a3-3df56e1cbb1d")
    insurer = (By.ID, "ab4f846d-5517-49f5-b2ee-469bdf7f1a86")
    reason = (By.ID, "62c213f5-d3fb-4b79-8836-dede756eb409")
    payment = ()
    request_date = (By.ID, "72f777bc-c7fe-4c76-b2a9-949baddaea70")
    request_number = (By.ID, "c861aeb5-965c-45e0-b299-7301159f7b62")
    manager = ()


class FSSRequestCardLocators(object):

    unit = (By.ID, "5d2b8d9e-1e82-4451-b05f-07e4109cd7fa")
    full_name = (By.ID, "770cce08-d376-4740-b8ac-f440e4777ca6")
    type = ()

    first_employer = (By.ID, "618da5d8-7b9f-4fc4-8d59-44fd42b8e075")
    first_itn = (By.ID, "635ed8e4-8bf6-44df-9e9a-cae5a251edf9")
    first_unit = (By.ID, "a9a39b5c-37ff-4fda-9bae-a822be750f84")
    first_kpp = (By.ID, "b2ae30a9-d8b4-445c-a7c9-ee64e8bd2323")
    first_registration_number = (By.ID, "dff42ec4-dc9a-42a6-bbac-3c8ea64f4e6b")
    first_additional_code = (By.ID, "e8d40833-39bf-40b7-81b1-71faa1a8cb48")
    first_code = (By.ID, "485abfdd-6a21-48b6-897c-90ce8f61939c")
    first_period_from = (By.ID, "f2380bf5-b507-4879-bb6e-e9b4a1d4bc66")
    first_period_to = (By.ID, "772bb1c1-7687-4a85-9b35-5cef5d5ef57f")

    second_employer = (By.ID, "b89f642b-6998-464e-b823-866be5a76383")
    second_itn = (By.ID, "34b72501-62b6-4fdf-a3b5-6c9e83908c17")
    second_unit = (By.ID, "a9a39b5c-37ff-4fda-9bae-a822be750f84")
    second_kpp = (By.ID, "b2ae30a9-d8b4-445c-a7c9-ee64e8bd2323")
    second_registration_number = (By.ID, "dff42ec4-dc9a-42a6-bbac-3c8ea64f4e6b")
    second_additional_code = (By.ID, "e8d40833-39bf-40b7-81b1-71faa1a8cb48")
    second_code = (By.ID, "485abfdd-6a21-48b6-897c-90ce8f61939c")
    second_period_from = (By.ID, "f2380bf5-b507-4879-bb6e-e9b4a1d4bc66")
    second_period_to = (By.ID, "772bb1c1-7687-4a85-9b35-5cef5d5ef57f")

    third_employer = (By.ID, "eeca9e2e-97c3-47fe-8ba9-f7b9094c6907")
    third_itn = (By.ID, "c09860a7-82ae-41d3-bb73-f50e87a573c7")
    third_unit = (By.ID, "491f654e-2fa7-4825-80cb-0f7cf43d927f")
    third_kpp = (By.ID, "169a7239-31f3-4067-9a1d-ef99fd131fcf")
    third_registration_number = (By.ID, "647f14ca-2faa-4f6a-84b2-c4d498f5eb2f")
    third_additional_code = (By.ID, "9742d776-52cc-476d-968d-f91ebc36eca5")
    third_code = (By.ID, "6e2e3e4e-314e-4b89-862c-d7a66ea5c254")
    third_period_from = (By.ID, "4ab09352-4b47-433f-98ee-73eb2ab79237")
    third_period_to = (By.ID, "73e18f10-7c55-47a7-9b3b-1361b2d4c443")

    request_date = (By.ID, "b7f45e48-8ec6-4a18-8d9b-1886b0feec00")


class FTNCardLocators(object):

    base = (By.ID, "6538d714-5fd7-43d3-b2d6-0b79521bf822")
    discount = (By.ID, "dfe2ca2a-21c0-4431-a3e4-62c0a54bbb03")
    privilege = (By.ID, "16dec506-8327-400b-8f12-ce2f66ecd26f")
    material_assistance = (By.ID, "d5157ad4-652a-4629-a395-38bbca113b3e")
    amount = (By.ID, "fc372929-734f-4c52-bf79-9844fc669bab")


class FSTNCardLocators(object):

    fund = (By.ID, "ef376bb4-d8f4-424a-8b3e-0734616f656f")
    base = (By.ID, "874d4370-f86a-40b5-9429-155c38be97ff")
    disabled_base = (By.ID, "6da397e3-737d-4c05-b5fd-02f8b3fa8239")
    discount = (By.ID, "974f4010-4765-4111-81fc-7cacadc62187")
    deductions = (By.ID, "4e3e83a9-1a1e-4340-8a3d-edf03c9c507a")
    disabled_deductions = (By.ID, "70a42227-b1e3-4613-bef1-f81bb323242e")
    material_assistance = (By.ID, "67dd8b18-f3fb-4751-846e-abad4b76d05d")
    amount = (By.ID, "78ff9283-c38d-46fb-bfab-e8dc53712637")


class DisabledCardLocators(object):

    full_name = (By.ID, "dd75cec4-5f83-45d0-ba70-6392747038b5")
    reference = (By.ID, "725f1727-61fe-41bd-9472-c3f8570170ba")
    reference_number = (By.ID, "9b94ee99-d9cd-475d-a143-02ba5e259664")
    date = (By.ID, "9ca59fe5-ab52-42f9-beaa-7a3fa750a137")
    group = (By.ID, "a8890d0e-3611-49a2-96ae-24069f6f6a10")
    validity = (By.ID, "675371b2-876a-4300-9467-7bb17299179c")


class PersonalAccountLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Л' and @role='tab']")
    add = (By.XPATH, "//button[@data-button-id='3274c2be-1ed3-4887-b014-2dadb892af22']")


class AccountInfoLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Сведения о лицевом счете' and @role='tab']")
    personnel_number = (By.ID, "e3fbe28d-0388-4a82-b73c-38a9f853c373")
    receipt_date = (By.ID, "b8df4b03-cbac-4e7c-91a4-9fae4b5828d0")
    order_number = (By.ID, "21ff380f-9f3b-4a68-b35e-4e6d21266130")
    salary_amount = (By.ID, "21624aa0-5032-4d25-9a01-629fd1ad56ca")
    working_hours = (By.ID, "436b442c-2091-4a97-88f7-0671171f5264")
    change_date = (By.ID, "2256927f-56f1-4b19-aab4-a8aec7e0d2d0")
    payment_category = ()
    payment_category_by = ()
    time_category = ()
    status_on = (By.ID, "19966bc1-ca51-48e8-9d08-a995e8a50c74")
    status_off = (By.ID, "05a0b5b3-e2fe-43c9-8555-1eb6f300fe43")
    ets = ()
    subdivision = (By.ID, "d3f70066-0c4f-4b88-8951-6e581a6e8166")
    position = (By.ID, "348ef3a5-0ccd-47b4-9bb4-ea11a4eaaf02")
    experience = (By.ID, "98b07606-b33d-4a9f-99e7-b8b9a1afe0ee")
    last_payroll = (By.ID, "ee5e7338-5688-45af-bad2-ede03fc352d0")
    dismissal_date = (By.ID, "0deb4cdd-83bc-41ef-81b8-add085db7fc7")
    fired = (By.ID, "67c8c098-63d0-41b6-bd2c-6221fba07ccb")
    dismissal_number = (By.ID, "6ff4eb15-07a9-4dde-ad15-e5dd5df8222d")
    dismissal_category = ()
    class_rank = (By.ID, "73690acb-6256-4439-8684-13d03f2e7761")
    union_member = (By.ID, "9c12ff6a-4475-478f-a579-f75c35621041")
    member_from = (By.ID, "59719605-8423-44c9-a027-068c934b5e50")
    member_to = (By.ID, "4162d135-0f17-4399-ac15-5663fc9a4f32")
    employee_number = (By.ID, "4709bfcb-a041-464c-bc49-cb807d6f5084")


class CalcInfoLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Сведения для расчета' and @role='tab']")
    holiday_payment = ()
    holiday_period_from = (By.ID, "8f904241-1a2f-4d63-8824-4418572c8258")
    holiday_period_to = (By.ID, "2c0baccf-652d-4975-b9a1-66a5cf1126af")
    note = (By.ID, "c139154e-8f78-41d0-bc1d-eca174530f16")
    sick_days_percent = ()
    average_daily_earnings = (By.ID, "d1c95fad-422b-47bd-be4a-35f02fc0a337")
    privileges_type = ()
    coefficient = (By.ID, "65cba738-f5eb-46cd-b467-9fd0c7ed3aef")
    state_employee = (By.ID, "b0be534f-b804-486f-bfc2-17cecc497f98")
    main_work = (By.ID, "c4a77973-4f35-40b0-812b-4a8e526f1a91")
    resident = (By.ID, "943e3709-ce7c-4f1a-89d4-e7123b22c2e9")
    pluralist = (By.ID, "aa39167e-1636-4c22-86da-85dd583420aa")
    chaes_member = (By.ID, "46b3aef3-7c7c-4939-9512-eed81e0d8f96")
    chaes_number = (By.ID, "a47c5af4-4848-457e-8049-443dc7b08eca")
    salary_without_rounding = (By.ID, "d077d142-429a-4bef-b986-bff70d3cd49d")
    income_tax = (By.ID, "f3bfd77a-ea05-42e6-96fc-b73788d11685")
    prepaid_expense = (By.ID, "064ac95e-f625-477c-ac2d-1d9a8756b383")
    region = ()
    alimony = ()
    stb_card = (By.ID, "d3f86d4f-261b-48d2-9751-0bbfd911e118")
    payment_method = ()
    card_number = (By.ID, "4a51b209-8796-438a-ab9b-dd2f6f43f790")
    full_name = (By.ID, "fe307635-205c-443f-a618-7ab6749ff10b")
    validity = (By.ID, "dbdbf28f-30f6-49f4-93f4-70a895d8940b")
    bank_list = (By.ID, "15a43606-e4cc-4755-b428-c9be19b7cf5c")
    key = (By.ID, "860f433b-0d88-42a8-8181-9f01a08ccb5e")


class EmployeePrivilegesLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Льготы на сотрудника' and @role='tab']")
    add = (By.XPATH, "//button[@data-button-id='39c5f3e8-9621-4b85-9d33-a4991e12e529']")
    date_start = (By.ID, "2c67dd54-8315-4dab-9d8f-36d57c51502f")
    date_end = (By.ID, "ce823f55-7bdb-4f0a-8003-74562b344de2")
    child_privilege = (By.ID, "8e9aeb06-40eb-41be-b0c1-69a6955943da")
    renouncement = (By.ID, "7507661a-5da8-4c8b-8c28-f9b74ec136eb")
    child_number = (By.ID, "a62ce7a0-a008-4738-9559-e4c7b2d599ae")
    statement_number = (By.ID, "304f5730-d96c-4069-9fce-c936a3a8931d")
    single_parent = (By.ID, "09489545-f03a-468b-bcbb-6e19d037f928")
    birthday = (By.ID, "80676bf7-562d-4400-8324-3ab3f8f4be14")
    statement_date = (By.ID, "6432b904-d7e1-4abe-b5ac-82f7afeb92a7")
    disabled = (By.ID, "a70777ba-4f15-4cf2-ae97-aa6d9eb2e93a")
    tax_deduction = (By.ID, "b138d81e-7075-446a-9dd6-22ad89404a38")
    tutor = (By.ID, "fe0d87ff-05f7-40e9-8bb0-320dfc434755")
    professional_deduction = (By.ID, "2e7df519-fcce-44ec-a9c9-10b10004887a")
    social_deduction = (By.ID, "758d7af3-94d9-4fa3-b7e4-06f8d0a1f64e")
    note = (By.ID, "ccde59e4-dfa2-4afb-9b02-0bb648c72d56")
    privileges_amount = (By.ID, "b5d6844e-dbae-4fd2-b174-be73a87259a9")
    deduction_code = (By.ID, "af1ede0d-d827-4022-8229-fff797e0c39c")
    deduction_sum = (By.ID, "c1734617-5f83-454e-aef5-3b51ea40ec9c")
    imns = (By.ID, "d37578ad-bf28-4153-8404-6b9bda76df24")
    notification_number = (By.ID, "d814d931-40ea-4cd2-a099-fcf2ddbf1184")
    notification_date = (By.ID, "db9daade-d812-4281-9daa-2a2198777977")
    submit = (By.XPATH, "(//button[normalize-space(text())='Сохранить'])[3]")


class WageIndexationLocators(object):

    def open(self):
        self.select_tab("Сведения о лицевом счете")


class HistoryLocators(object):

    def open(self):
        self.select_tab("Сведения о лицевом счете")


class DocumentsLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Документы' and @role='tab']")
    document_type = ()
    serial_first = (By.ID, "7d953825-eb62-4559-94c6-db6ec10c72c8")
    serial_second = (By.ID, "8dd2b8a7-9208-48a5-8d56-511658b17bf5")
    serial_third = (By.ID, "b9630cfb-3929-4988-b21d-685760038333")
    department_code = (By.ID, "57fbdc82-e447-4a74-973c-3ebc57f9e5f5")
    issue_date = (By.ID, "dc5a3b00-989f-49c8-a52d-010295c1000a")
    issued_by = (By.ID, "bb75ef45-9df1-4e9d-be3f-4f21ed7aa5e5")


class AddressesLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Адреса' and @role='tab']")
    index = (By.ID, "e5743a87-5de7-4fe3-8b4d-67409d7a74c1")
    region = (By.ID, "1d2a681f-53de-43d5-9948-f0e53f5c3725")
    area = (By.ID, "c7379406-6410-4611-9f09-d6831aba9be2")
    area_type = (By.ID, "9170e315-8a88-4308-8d9d-ac30a16e37be")
    city = (By.ID, "b461c1cc-97e3-4710-a7a4-ecb4bf308991")
    city_type = (By.ID, "27e5a7ac-6549-4e6b-90e7-520095ada440")
    locality = (By.ID, "b1b4ff70-8d1f-4ef5-8ff5-02a908bb4f78")
    locality_type = (By.ID, "c409c1c7-87dd-4783-9c87-cf94c8ef440b")
    street = (By.ID, "b3d36c66-7b89-41d8-bfcc-3d215f52b5eb")
    street_type = (By.ID, "d37d0201-ca80-4f7b-8fb8-7de3e6dd11dc")
    building = (By.ID, "7f7d78a3-3d40-49cc-8323-8d571391d48a")
    block = (By.ID, "e1da301c-0906-4173-9e8e-ff5cc9d78b7e")
    apartment = (By.ID, "892720fc-a436-47e9-beb7-d856020f528e")
    use = (By.ID, "9c48f71d-dad1-4107-9d75-263ebea0b3f3")
    actual_address = (By.ID, "cac01c8a-5228-4d5c-b886-4569475c579e")


class PFRLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Данные ПФР' and @role='tab']")
    registration_number = (By.ID, "a48b985b-b430-4be4-aa70-9fa7328cd3b5")
    category = ()
    locality_type = ()
    retirement_date = (By.ID, "1f66969f-770c-4e12-ab30-e3b91a812a45")
    esn = (By.ID, "b884be41-de26-44f9-a560-005448089148")
    last_name = (By.ID, "b0136ebd-37a9-45a7-b9b5-b36aa0e79557")
    first_name = (By.ID, "b0cb498d-bc2d-473b-8fb0-186ad1c14832")
    middle_name = (By.ID, "b7fe1464-6831-42d3-b58e-268de64659a0")
    nationality = (By.ID, "10fb8fd7-9773-46cf-9bce-843dcb87f04a")
    exclude = (By.ID, "e7362933-5b22-4fb5-8349-db723b4d43e3")
    country = (By.ID, "0635fddd-8528-4608-8bf8-f29cd0732ed3")
    region = (By.ID, "73c61c49-5abe-4746-afb3-a26f14604fcd")
    area = (By.ID, "018fadb0-450a-4fc2-8fbf-59cfd7e618d5")
    city = (By.ID, "41137b78-0788-43ca-9d89-38c186bfe0e8")


class FNSLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Данные ФНС' and @role='tab']")
    itn = (By.ID, "32d9001d-9547-47b3-8b79-8e8efa43c589")
    exclude = (By.ID, "d9c6ead0-a17f-447b-880e-c375162c1c22")
    resident = (By.ID, "ff9320e0-63e7-4890-9f0a-d93504866da7")
    nationality = ()


class FullNameLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='История ФИО' and @role='tab']")


class OtherLocators(object):

    tab = (By.XPATH, "//a[normalize-space(text())='Прочее' and @role='tab']")
    requisites = (By.ID, "22eca8f3-1a1a-4ffc-ac9c-6ce14bf84d18")
    phone_number = (By.ID, "fd3d8bcf-c43e-407d-84a5-969154f26bd2")
    email = (By.ID, "43e0066d-d1f1-4024-8799-07dafe2127e3")
    crimea = (By.ID, "11afc8c4-5905-4743-9587-625e72304246")


class PayrollWithholdingLocators(object):

    prev_month = (By.XPATH, "//span[@class='qa-icon-prev-month']")
    next_month = (By.XPATH, "//span[@class='qa-icon-next-month']")
    add = (By.XPATH, "//button[contains(., 'Добавить')]")
    payroll = (By.XPATH, "//a[@data-button-id='85d1d62c-be8d-41f8-b859-0c0ea5eeaa71']")
    withholding = (By.XPATH, "//a[@data-button-id='eb50aa7e-0cbc-4bc4-a869-8c39bbcc4d39']")
    addition_input = (By.XPATH, "//button[contains(., 'Дополнительный ввод')]")
    requests = (By.XPATH, "//a[.='Запросы для б/л']")
    members_statement = (By.XPATH, "//a[@data-button-id='356a65aa-19fa-45d0-888e-d6f43f3f4b3d']")
    pf_request = (By.XPATH, "//a[@data-button-id='d4729f8c-5c28-4f6e-b9ae-82ccd732f253']")
    fss_request = (By.XPATH, "//a[@data-button-id='e19e51d6-1e07-458d-8e83-4de498d6b8a3']")
    income_certificate = (By.XPATH, "//a[@data-button-id='061457bc-e6c2-4a8c-b78c-b4e8cd00ec10']")
    data_funds = (By.XPATH, "//button[contains(., 'Данные о внеб')]")
    data_ftn = (By.XPATH, "//a[@data-button-id='f3a383b0-6a94-4315-9ecb-2fab0f740f46']")
    data_fstn = (By.XPATH, "//a[@data-button-id='b91f0f96-5777-46c2-97da-babbda123519']")
    reference_previous_place = (By.XPATH, "//a[@data-button-id='0adf9a17-63bb-4943-9297-7cb3ede4e157']")
    employee_reports = (By.XPATH, "//button[contains(., 'Отчеты по сотруднику')]")
    settlement_sheet = (By.XPATH, "//a[@data-button-id='2a5b6b92-8d65-4aea-ba28-d79c7e36571a']")


class PayrollCardLocators(object):

    order = (By.ID, "f8f84656-1743-4883-8179-bc72c529c829")
    date = (By.ID, "f1effdd5-2af4-4e11-bc88-099634ff0ab2")
    date_from = (By.ID, "d440192c-25ff-4db6-ae99-e024a12978b4")
    date_to = (By.ID, "809f1d24-384f-4827-a0a7-737c760b4d4b")
    payroll_sum = (By.ID, "969b6337-0451-49f1-bf18-a39470374c12")
    average_income_sum = (By.ID, "357c270b-d776-44b0-baf8-1c857b925378")
    assessed_date = (By.ID, "da91995c-4438-46d2-bcad-53e9fcd40a1a")
    awarded_date = (By.ID, "dc040caa-2e1b-4d08-9518-340687241cf6")
    validity = (By.ID, "4da9fc57-4b3c-45c1-94d8-23ffa3032030")
    recalculate = (By.ID, "952eab5c-d74a-47b2-9363-9c459a007b1b")
    quantify_ban = (By.ID, "345d2446-f8b6-4dea-9cc0-599e734d0244")
    count_days = (By.ID, "3e748e5c-e6e4-4e2d-9641-9d7f83e0d0bf")
    parameters = [
        (By.ID, "2140dbc7-abf5-49b0-83ea-59f08491297d"),
        (By.ID, "fcde0563-6986-4b87-b199-d56332bf0eed"),
        (By.ID, "c133192e-2b65-4e62-99bc-dfb5a111fc41"),
        (By.ID, "389a67ba-d3d1-454a-ad9a-dc30dbd4f466"),
        (By.ID, "7ce951dc-a52f-45e7-8a9d-a40e6a043e63"),
        (By.ID, "20533d9f-c1e1-4041-8371-8b2e4e68dea5"),
        (By.ID, "2bb68e38-babc-4598-b452-7d88a482dd47"),
        (By.ID, "905b769b-732f-4470-b26a-40f282d13df8"),
        (By.ID, "172f1066-b396-416c-9390-914e985bd50b")
    ]
    group = (By.ID, "4bda3e8d-921c-4689-be9e-5e95c64258b5")
    financing = (By.ID, "39d87d4d-eb53-4a61-9692-58c6b01921b4")
    costs = (By.ID, "befd12ed-e020-4cf4-8e92-9bcf93cf7498")


class WithholdingCardLocators(object):

    order = (By.ID, "619e1a05-b117-49ff-99d8-ec9eff80bfd9")
    withholding_sum = (By.ID, "81162bb2-30a6-422a-8574-e4e787aa8a2a")
    validity = (By.ID, "e77800ec-d229-4549-bdb4-803df7546603")
    assessed_date = (By.ID, "65fd774a-e3a9-4dcc-b0df-d2f0c4a736d5")
    awarded_date = (By.ID, "38bceb8f-4e3d-4123-ada8-169e0692c814")
    quantify_ban = (By.ID, "8582f563-20de-43f4-b969-dc4d24f31d89")
    recalculation = (By.ID, "8d1f0a3d-32f5-4ee3-8ef9-01ecb43a0071")
    parameters = [
        (By.ID, "c777e03b-5931-483a-acff-3829aa1f1817"),
        (By.ID, "e3c58924-5c16-4961-87fc-72fc3d743624"),
        (By.ID, "c5596f8f-d2f9-459b-aaaf-f0311e662234"),
        (By.ID, "d9b3f6bf-6eb5-4361-aa61-5bc0e23a2954"),
        (By.ID, "d257449b-ee2b-4398-b2f2-f1a8ed3c3e8d"),
        (By.ID, "091f0c59-fd07-4dd4-8921-2f6edc0519a1"),
        (By.ID, "d2c4aa90-f5fb-4c21-b74b-0aaf5b551655"),
        (By.ID, "bec061a6-a202-4248-960e-92ce497f5e43"),
        (By.ID, "69568ce3-3cfc-4b18-8d22-12a24918d758")
    ]
    payment_accruals = (By.ID, "1c5ecea1-9f93-440c-ae36-4154bcee025f")
    executive_sheet = (By.ID, "387274e2-8c42-4e09-88e0-335a7aae62ec")


class IncomeCertificateLocators(object):

    add = (By.XPATH, "//a[@data-button-id='9c4dda88-e882-42d5-898e-1cc183da0eae']")
    date = (By.ID, "1aa771e0-dd11-49bc-9585-1c0cd77d3076")
    tax_sum = (By.ID, "aaa7e377-2967-4224-bfd8-cddc4df31940")
    income_sum = (By.ID, "33215267-234e-43d5-80f5-4608b700d71c")
    income_type = (By.ID, "1c96b083-84d5-407d-b87a-83d796e29f51")
    deduction_sum = (By.ID, "91dc80eb-8735-4593-a4de-e6dd2d3e7700")
    deduction_type = (By.ID, "587370bc-2ab4-441a-af33-e9340b4c4d5d")
    childs_amount = (By.ID, "73dcb52e-974d-40e7-bf53-0c6681fd79de")
    submit2 = (By.XPATH, "(//button[.='Сохранить'])[2]")


class ReferencePreviousPlaceLocators(object):

    issue_date = (By.ID, "d4fba5d4-44cf-475a-b573-5d2d678f58ff")
    reference_number = (By.ID, "a930b8ef-e397-4b09-ac54-444102502d6a")
    insurer = (By.ID, "20234d8f-4e99-4a7b-9e87-85dd0ac5f907")
    periods_period_from = (By.ID, "86c77c3b-27ff-463c-9dc3-7946781b5dbf")
    periods_period_to = (By.ID, "d126ad92-ea15-4a51-aa0e-299407f0fbba")
    periods_include = (By.ID, "6846aa50-ffac-4739-8242-47cd13dc94b1")
    salary_year = (By.ID, "acbf1bbc-e69e-4c79-9076-187ed8de9bb5")
    salary_sum = (By.ID, "3708cf3e-f79f-4611-b13f-d6f6a0b01731")
    salary_include = (By.ID, "ed1c3511-dc88-456d-8760-42c851899b89")
    days_year = (By.ID, "bb8c67fd-623d-479c-9dcd-c496238787a7")
    days_period_from = (By.ID, "5dc36048-1e90-48d0-9064-50a61052433a")
    days_period_to = (By.ID, "97f2ac62-38f8-4453-bcad-4bbf60cb2ae7")
    days_amount = (By.ID, "ab1fadf7-f9ef-4cd8-b0ad-df43a6f74c82")
    days_name = ()
    days_include = (By.ID, "9b39761c-9b3e-45be-9c44-a579beaccb8b")


