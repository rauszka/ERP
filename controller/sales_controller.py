from model.sales import sales
from view import terminal as view


BETWEEN = ["Start", "End"]
LABELS = ["ID", "Distributor", "Title", "Revenue", "Premier"]


def add_transaction():
    table = view.get_inputs(LABELS[LABELS.index('Distributor'):])
    sales.add_transactions(table)
    

def list_transactions():
    data = sales.list_transactions()
    data.insert(0,LABELS)
    view.print_table(data)
    

def update_transaction():
    table = view.get_inputs([LABELS[0]])
    if sales.check_id(table):
        data = view.get_inputs(LABELS[1:])
        sales.update_transaction(table,data)
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
    view.print_general_results(data, 'The movie which generated the biggest transaction')


def get_biggest_revenue_product():
    data = sales.get_biggest_revenue_product()
    view.print_general_results([data], 'The movie which generated the biggest revenue')
    

def count_transactions_between():
    start, end = view.get_inputs(BETWEEN[0:])
    start1 = sales.convert_date(start)
    end1 = sales.convert_date(end)
    result =sales.number_of_transactions_between(start1,end1)
    view.print_general_results([result], f'Transactions between {start} and {end}')
    

def sum_transactions_between():
    start, end = view.get_inputs(BETWEEN[0:])
    start1 = sales.convert_date(start)
    end1 = sales.convert_date(end)
    result = sales.sum_of_transactions_between(start1, end1)
    view.print_general_results([result], f'Sum of transactions between {start} and {end}')
    

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
               "Add new movie",
               "List movies",
               "Update movie",
               "Remove movie",
               "Get the movie that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of movies between",
               "Sum the price of movies between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        view.print_message('\n')
        view.print_message(sales.get_random_quote())
        view.print_message('\n')
        try:
            view.print_message('\n')
            operation = view.get_input("Please select an operation: ")
            view.print_message('\n')
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
