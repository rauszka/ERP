from model.data_manager import read_table_from_file
from model.sales import sales
from view import terminal as view
import alma


BETWEEN = ["Start", "End"]
LABELS = ["ID", "Name", "Category", "Weight", "Date of birth"]


def add_transaction():
    table = view.get_inputs(LABELS[LABELS.index('Name'):])
    sales.add_transactions(table)
    

def list_transactions():
    data = sales.list_transactions()
    data.insert(0, LABELS)
    view.print_table(data)
    

def update_transaction():
    table = view.get_inputs([LABELS[0]])
    if sales.check_id(table):
        data = view.get_inputs(LABELS[1:])
        sales.update_transaction(table, data)
    else:
        view.print_message("The ID doesn't exist.")


def delete_transaction():
    table = view.get_inputs([LABELS[0]])
    if sales.check_id(table):
        sales.delete_transaction(table)
    else:
        view.print_message("The ID doesn't exist.")


def get_biggest_revenue_transaction():
    data = sales.get_biggest_revenue_transaction()
    view.print_general_results(data, 'The heaviest contestant')


def get_biggest_revenue_product():
    data = sales.get_biggest_revenue_product()
    view.print_general_results([data], 'The heaviest contestant')
    

def count_transactions_between():
    start, end = view.get_inputs(BETWEEN[0:])
    start1 = sales.convert_date(start)
    end1 = sales.convert_date(end)
    result = sales.number_of_transactions_between(start1, end1)
    view.print_general_results([result], f'Contestants born between {start} and {end}')
    

def sum_transactions_between():
    data = read_table_from_file("./model/sales/sales.csv")
    weights = []
    age = []
    for people in data:
        weights.append(people[3])
        age.append(people[4][0:4])

    alma.show_chart(age, weights)
    

def run_operation(option):
    if option == 1:
        add_transaction()
    elif option == 2:
        list_transactions()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "Add new contestant",
               "List contestants",
               "Update data",
               "Remove contestant(s)",
               "Get the heaviest contestant",
               "Get the category that has the heaviest contestants altogether",
               "Count contestants born movies between",
               "Show weight:age diagram"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        view.print_message('\n')
        try:
            view.print_message('\n')
            operation = view.get_input("Please select an operation: ")
            view.print_message('\n')
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
