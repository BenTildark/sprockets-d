"""
Write a program to ask the user to enter their first and family names using a mixture of upper and lower case characters and have them displayed in uppercase, lowercase and correctly capitalised formats.


Your program must display the following message:

Please enter your first name using upper and lower case characters:

Your program must then ask the user to enter their family/surname as follows:

Please enter your last name using upper and lower case characters:

then display the following messages

FirstName, your first name in lower case is FirstNameInLowerCase.

Your first name in upper case is FirstNameInUpperCase.

Your first name correctly capitalised is FirstNameCorrectlyCapitalised.

Your last name correctly capitalised is LastNameCorrectlyCapitalised.

Your full name correctly capitalised is FullNameCorrectlyCapitalised.

where

FirstName is the users first name and is displayed correctly capitalised.
FirstNameInLowerCase is their first name displayed completely in lower case.
FirstNameInUpperCase is their first name displayed completely in upper case.
FirstNameCorrectlyCapitalised is their first name displayed correctly capitalised.
LastNameCorrectlyCapitalised is their last name displayed correctly capitalised.
FullNameCorrectlyCapitalised is their concatenated first and last names correctly capitalised.


FullNameCorrectlyCapitalised must be correctly spaced with one space between the first and last names.



Example


Please enter your first name using upper and lower case characters: dAvE
Please enter your last name using upper and lower case characters: bRACkEn
Dave, your first name in lower case is dave.
Your first name in upper case is DAVE.
Your first name correctly capitalised is Dave.
Your last name correctly capitalised is Bracken.
Your full name correctly capitalised is Dave Bracken.



Ensure you test your code using the following data and that the program displays the correct output for each.

First name: FrED           Surname: BloGGs

First name: frED            Surname: bloGGs

First name: fred             Surname: BLOGGS

First name: FRED         Surname: bloggs

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name using upper and lower case characters: "
# "Please enter your last name using upper and lower case characters: "
# "{}, your first name in lower case is {}."
# "Your first name in upper case is {}."
# "Your first name correctly capitalised is {}."
# "Your last name correctly capitalised is {}."
# "Your full name correctly capitalised is {}."

first_name = input("Please enter your first name using upper and lower case characters: ")
last_name = input("Please enter your last name using upper and lower case characters: ")


def characterize(first_arg, second_arg):

    full_name = "{} {}".format(first_arg.capitalize(), second_arg.capitalize())

    components = ["{}, your first name in lower case is {}.".format(first_arg.capitalize(), first_arg.lower()),
                  "Your first name in upper case is {}.".format(first_arg.upper()), "Your first name correctly capitalised is {}."
                  .format(first_arg.capitalize()), "Your last name correctly capitalised is {}.".format(second_arg.capitalize()),
                  "Your full name correctly capitalised is {}.".format(full_name)]
    for i in components:
        print(i)


characterize(first_name, last_name)
