""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from controller.sales_controller import get_biggest_revenue_transaction
from model import data_manager, util


DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def add_employees(table):
    table = table
    table.insert(0, util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"))
    temp_list = data_manager.read_table_from_file(DATAFILE, separator=';')
    temp_list.append(table)
    data_manager.write_table_to_file(DATAFILE, temp_list, separator=';')


def list_employees():
    hr_data = data_manager.read_table_from_file(DATAFILE)
    return hr_data


def check_id(table):
    table = ''.join(table)
    data = data_manager.read_table_from_file(DATAFILE)
    id = []
    for line in data:
        id.append(line[0])
    if table in id:
        return True
    else:
        return False


def update_employee(table, data):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    table = ''.join(table)
    for dicts in list:
        if dicts[0] == table:
            dicts[1] = data[0]
            dicts[2] = data[1]
            dicts[3] = data[2]
            dicts[4] = data[3]
    data_manager.write_table_to_file(DATAFILE, list, separator=';')


def delete_employee(table):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    table = ''.join(table)
    temp_list = []
    for dicts in list:
        if dicts[0] != table:
            temp_list.append(dicts)
        else:
            continue
    data_manager.write_table_to_file(DATAFILE, temp_list, separator=';')


def convert_date(date):
    date = ''.join(date).replace('-', '')
    year =  (int(date[:4]) - 1900) * 365
    day = int(date[-2:])
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_months = sum(months[:int(date[4:6])])
    leap_year = 0
    for i in range(1900, int(date[:4]), 4):
        if i % 400 == 0:
            leap_year += 1
        if i % 100 == 0:
            continue
        if i % 4 == 0: 
            leap_year += 1
    number = year + sum_months + day -30 + leap_year
    return number


def get_oldest_youngest():
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    for i in list:
        i[2] = convert_date(i[2])
    oldest = sorted(list,key=lambda y: y[2])
    youngest = sorted(list, key=lambda y: y[2])
    return oldest[0][1], youngest[-1][1]


def get_average_age(today):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    ages = []
    for i in list:
        ages.append(int((convert_date(today) - convert_date(i[2]))/365))
        
    return (int(sum(ages) / len(ages)))


def has_birthday_within_two_weeks(today):
    replace_today = ''.join(today).replace('-', '')
    today_digit = convert_date(today)
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    replacement = replace_today[:4]
    employees = []
    for i in list:
        i[2] = i[2].replace(i[2][0:4], replacement)
    for i in list:
        if 0 <= convert_date(i[2]) - convert_date(today) <= 14 or convert_date(today) - (convert_date(i[2])) >= 351:
            employees.append(i[1])
    return employees


def clearance(number):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    number = "".join(number)
    counter = 0
    for i in list:
        if int(i[4]) >= int(number):
            counter += 1
    return counter


def count_employees_per_department():
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    departments = []
    numbers = []
    for i in list:
        departments.append(i[3])
    for i in sorted(set(departments)):
        x = departments.count(i)
        numbers.append(x)
    keys = sorted(set(departments))
    dicts = dict(zip(keys, numbers))
    return dicts

def get_random_quote():
    quote = util.generate_quote()
    return quote