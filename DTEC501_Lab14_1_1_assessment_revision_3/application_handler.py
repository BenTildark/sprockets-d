"""
FUNCTIONS MODULE
-----------

Create a function called file_exists

file_exists requires 1 parameter

datafile

datafile contains the name of the file where the data for the application is stored.

If the file that datafile refers to is present then the file_exists function returns True.

If the file that datafile refers to is not present then the file_exists function returns False.

Hint.

For this question, the data file will be in the same working directory as your
code so specify the filename, not the path.

Example test code and output

print(file_exists("ThisFileIsPresent.txt"))

True

print(file_exists("ThisFileIsNotPresent.txt"))

False

"""
import os

# Student: Michael Devenport
# Email: croxleyway@gmail.com


def file_exists(datafile):

    """returns True if file exists in cwd else False"""
    if os.path.exists(datafile):
        return True
    else:
        return False


# print(file_exists('example_tests_output.py'))


"""
Create a function called update_file

update_file requires 3 parameters

shop, cost, and datafile

shop is the name of the shop to be put in the file. shop is a string.
cost is the cost difference of the item in the shop. cost is an integer. 
datafile is the name of the file containing the data for the application.
datafile is always in the same directory as the program. In Moodle (JobEngine), the file name is case sensitive.
 
The update_file function does not check to see if datafile is already present,
it merely writes data to the file even if it is present.

The update_file function writes the data in datafile in a single line in the following format:

shop,cost

There is no CrLf (\n) at the end of the line.

There is only ever one line of data in the file.

The update_file function returns None.

Example test code and output
 
update_file("Countdown",19,"CheapShop.txt")

If you open CheapShop.txt in an editor you will see it contains

Countdown,19

There should not be any output but if you open CheapShop.txt in an editor, it should look like:

Countdown,9

"""


def update_file(shop, cost, datafile):

    """Create or overwrite data to given file in cwd"""

    df = open(datafile, 'w')
    df.write(shop + "," + str(cost))
    df.close()

# print(update_file("Countdown", 17, "CheapShop.txt"))


"""
Create a function called display_file

display_file requires 1 parameter

datafile

datafile is the name of the file where the data for the application is stored
The display_file function returns None.

The display_file function does not check to see if datafile is present.
That is the responsibility of another section of code.

The display_file function displays the contents of the datafile as follows:

Shop: <Shop name> Cost: <Item cost>

Example test code and output
 
the_shop = "Aldi"
the_cost = 49
the_file = "CheapShop.txt"

update_file(the_shop,the_cost,the_file)
display_file(the_file)

Shop: Aldi Cost: 49 

Example test code and output

the_shop = "Countdown"
the_cost = 1
the_file = "CheapShop.txt"

update_file(the_shop,the_cost,the_file)
display_file(the_file)

Shop: Countdown Cost: 1

"""


def display_file(datafile):

    """Prints a given files content."""

    df = open(datafile, "r")
    entries = df.read().split(',')
    print("Shop: {} Cost: {}".format(entries[0], entries[1]))
    df.close()

# display_file("CheapShop.txt")


"""
Create a function called display_menu

display_menu requires 0 parameters.

The display_menu function returns None.

The display_menu function prints the following menu.

Please select the number from one of the following options.
1) Enter shop and cost difference details.
2) Display the shop and cost difference details in the file.
3) Exit.

There are no blank lines at the start or at the end.

"""


def display_menu():

    """Displays application menu."""

    print("Please select the number from one of the following options.")
    print("1) Enter shop and cost difference details.")
    print("2) Display the shop and cost difference details in the file.")
    print("3) Exit.")


# display_menu()


"""
Create a function called get_price_difference

get_price_difference requires 1 parameter

datafile

datafile is the name of the file where the data for the application is stored
The get_price_difference function returns an integer.

The integer that needs to be returned is the last character in the line of text in the file. 

The get_price_difference function does not check to see if datafile is present.
That is the responsibility of another section of code.

 

Hint.

The code is very similar to that of the display_file function.
 
Example test code and output
 
the_shop = "Aldi"
the_cost = 2
the_file = "CheapShop.txt"

update_file(the_shop,the_cost,the_file)
difference = get_price_difference(the_file)

print(difference)

2 

Example test code and output

the_shop = "Countdown"
the_cost = 1
the_file = "CheapShop.txt"

update_file(the_shop,the_cost,the_file)
difference = get_price_difference(the_file)

print(difference)

1

"""


def get_price_difference(datafile):

    """returns the cost attribute of the data string as integer"""

    df = open(datafile, "r")
    value = df.read().split(',')[1]
    df.close()
    return int(value)


# print(get_price_difference("CheapShop.txt"))















