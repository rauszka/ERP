from model.crm import crm
from view import terminal as view

LABELS =  ["ID", "Name", "Email", "Subscribed"]


def add_customer():
    table = view.get_inputs(LABELS[1:])
    crm.add_customers(table)

def list_customers():
    data = crm.list_customers()
    data.insert(0, LABELS)
    view.print_table(data)
    

def update_customer():
    table = view.get_inputs([LABELS[0]])
    if crm.check_id(table):
        data = view.get_inputs(LABELS[1:])
        crm.update_customers(table, data)
    else:
        view.print_message("The ID doesn't exist.")


def delete_customer():
    table = view.get_inputs([LABELS[0]])
    if crm.check_id(table):
        crm.delete_customers(table)
    else:
        view.print_message("The ID doesn't exist.")


def get_subscribed_emails():
    subscribed_emails = crm.subscribed_emails()
    view.print_general_results(subscribed_emails, LABELS[3])
    

def run_operation(option):
    if option == 1:
        add_customer()
    elif option == 2:
        list_customers()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "Add new customer",
               "List customers",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        view.print_message('\n')
        view.print_message(crm.get_random_quote())
        view.print_message('\n')
        try:
            view.print_message('\n')
            operation = view.get_input("Please select an operation: ")
            view.print_message('\n')
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)