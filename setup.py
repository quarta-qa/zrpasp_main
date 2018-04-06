import json


def load_data(file_name):
    return json.loads(open('test_data/%s.json' % file_name, encoding="utf8").read())


def get_employee_by_index(data, n):
    return data["employee"][n]


def get_account_by_index(data, n):
    return data["user"][n]


def get_employee_by_name(data, value):
    for i in data["employee"]:
        if value == i["lastName"]:
            return i
    return None


def get_account_by_name(data, value):
    for i in data["user"]:
        if value == i["username"]:
            return i
    return None


class Links(object):
    main_page = "http://qtestzrpasp3.office.quarta-vk.ru:1090/"
    login_page = "%s/account/login"