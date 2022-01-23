from controller.crm_controller import LABELS


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f'{title}:')
    temp_list = []
    for key, value in enumerate(list_options):
        temp_list.append(f'({key}) {value}')
    list_options1 = temp_list[1:]+[temp_list[0]]
    for i in list_options1:
        print(i)


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)
    


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print("\n")
    print(f'{label}: \n ')
    for i in range(len(result)):
        print(f'{result[i]}')
    print("\n")



# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    splitter_line = []
    splitter = " | "
    splitter_forline = "-|-"
    table_len = []
    header = table[0]
    for i in range(len(header)):
       length = 0
       for j in range(len(table)):
           if len(table[j][i]) > length:
               length = len(table[j][i])
       table_len.append(length)

    print(f' /{"-" * (sum(table_len) + (len(splitter) * (len(table_len))) - 1)}\\')
    for i in range(len(header)):   
        splitter_line.append(f'{splitter_forline}{"-" * table_len[i]}')
    splitter_line = ''.join(splitter_line)[1:]
    for i in range(len(table)):
        lines = []
        for j in range(len(table[i])): 
            lines.append(f'{splitter}{table[i][j].center(table_len[j])}') 
        lines = "".join(lines)
        if i != 0:
            print(f' {splitter_line}{splitter_forline[:-1]}')
        print(f'{lines}{splitter}')
    print(f' \\{"-" * (sum(table_len) + (len(splitter) * (len(table_len))) - 1)}/')


def get_input(label):
    """Gets single string input from the user.
    
    Args:
        label: str - the label before the user prompt
    """
    mode = input(label )
    return mode
    


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    list = []
    for i in labels:
        x = input(f'{i}: ')
        list.append(x)
    return list


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)
