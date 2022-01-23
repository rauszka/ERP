""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util


DATAFILE = "model/sales/sales.csv"
HEADERS = ["ID", "Distributor", "Title", "Revenue", "Premier"]


def add_transactions(table):
    table = table
    table.insert(0, util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"))
    temp_list = data_manager.read_table_from_file(DATAFILE, separator=';')
    temp_list.append(table)
    data_manager.write_table_to_file(DATAFILE, temp_list, separator=';')


def list_transactions():
    sales_data = data_manager.read_table_from_file(DATAFILE)
    return sales_data


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


def update_transaction(table, data):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    table = ''.join(table)
    for dicts in list:
        if dicts[0] == table:
            dicts[1] = data[0]
            dicts[2] = data[1]
            dicts[3] = data[2]
            dicts[4] = data[3]
    data_manager.write_table_to_file(DATAFILE, list, separator=';')


def delete_transaction(table):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    table = ''.join(table)
    temp_list = []
    for dicts in list:
        if dicts[0] != table:
            temp_list.append(dicts)
        else:
            continue
    data_manager.write_table_to_file(DATAFILE, temp_list, separator=';')


def get_biggest_revenue_transaction():
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    biggest = []
    transaction = []
    for i in list:
        biggest.append(float(i[3]))
    for i in list:
        if max(biggest) == float(i[3]):
            transaction.append(i)
    return transaction


def get_biggest_revenue_product():
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    revenues = {}
    for i in list:
        key = i[1]
        value = i[3]
        if key in revenues:
            revenues[key] += float(i[3])
        else:
            revenues[key] = float(i[3])
    biggest = sorted(revenues.items(), key=lambda v: v[1], reverse = True)

    return biggest[0][0]


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


def number_of_transactions_between(start,end):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    number_of_days = 0
    for i in list:
        if convert_date(i[4]) >= start and convert_date(i[4]) <= end:
            number_of_days += 1
    return number_of_days


def sum_of_transactions_between(start,end):
    list = data_manager.read_table_from_file(DATAFILE, separator=';')
    sum_of_transactions = 0
    for i in list:
        if convert_date(i[4]) >= start and convert_date(i[4]) <= end:
            sum_of_transactions += float(i[3])
    return sum_of_transactions
    

def get_random_quote():
    quote = util.generate_quote()
    return quote