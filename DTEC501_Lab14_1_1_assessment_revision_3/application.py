"""
Create an application which keeps track of the shop and price difference which is selling the cheapest TV in the city.

The application will display previous menu when running.

Assume the user will always enter an integer as the option.

If the user enters 1 then ask the user to enter the name of the shop and the cost difference of the item.  

If the file does not exist, write the shop and the cost difference to the file in the format as specified in the
earlier question.  

If the file does exist, use the functions you have created to read the file and if the cost
difference of the item just entered by the user is cheaper (it's <) than the cost in the file, update
the file with the data the user just entered in the format as specified in the earlier question.
If the cost of the item just entered by the user is not cheaper than the cost in the file, inform the user 
that the shop in the file is cheaper than the one they entered.

If the user enters 2 then if the file exists, display the shop and cost that are in the file.

If the user enters 2 then if the file does not exist, then inform the user that no data file is present.

If the user enters 3 then display "Bye." and stop running the program.

In Moodle (CodeRunner), the data file will be in the same directory as the program.

Your code must make use of the display_file, file_exists, update_file, display_menu and get_price_difference functions
you have created for this lab as part of answering the previous questions. 
Place all your functions inline, do not import your functions from a module for this question. 

"""
# from application_handler import *
import os

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# The Function array


def file_exists(datafile):

    """returns True if file exists in cwd else False"""

    if os.path.exists(datafile):
        return True
    else:
        return False


def update_file(shop, cost, datafile):

    """Create or overwrite data to given file in cwd."""

    _df = open(datafile, 'w')
    _df.write(shop + "," + str(cost))
    _df.close()


def display_file(datafile):

    """Prints a given files content."""

    _df = open(datafile, "r")
    entries = _df.read().split(',')
    print("Shop: {} Cost: {}".format(entries[0], entries[1]))
    _df.close()


def display_menu():

    """Displays application menu."""

    print("Please select the number from one of the following options.")
    print("1) Enter shop and cost difference details.")
    print("2) Display the shop and cost difference details in the file.")
    print("3) Exit.")


def get_price_difference(datafile):

    """returns the cost attribute of the data string as integer"""

    _df = open(datafile, "r")
    value = _df.read().split(',')[1]
    _df.close()
    return int(value)


# The Application

shop_cost_diff = 1
show_shop_cost_diff = 2
exit_program = 3

df = 'CheapShop.txt'

selection = ''

while selection != exit_program:

    display_menu()

    selection = input("Option: ")

    if selection.isnumeric():
        selection = int(selection)

    if selection == shop_cost_diff:
        shop_name = input("Enter shop name: ")
        item_cost = input("Enter item cost: ")
        if file_exists(df):
            saved_price = get_price_difference(df)
            if int(item_cost) < saved_price:
                print("{} is cheaper. Updating the file.".format(shop_name))
                update_file(shop_name, int(item_cost), df)
            else:
                print("The shop on file is cheaper. The file has not been updated.")
        else:
            update_file(shop_name, int(item_cost), df)
            print("The file has been created.")

    elif selection == show_shop_cost_diff:
        if file_exists(df):
            display_file(df)
        else:
            print("No data file is present.")

print("Bye.")
