"""
Write a program which asks the user to enter their first name followed by a number between 0 and 10 inclusively.  Based on the value entered, display a suitable message.

Ask the user to enter their first name.

Please enter your first name:

The user will enter their <FirstName> at this point.

The program should output the following message:
<FirstName>, please enter an integer between 0 and 10 inclusively:

The program should then test to see if the <EnteredInteger> is in range 0 to 10 inclusively.

If <EnteredInteger> is in that range then test to see if it is less than 5, equal to 5 or greater than 5 and display the appropriate message from the following:

<EnteredInteger> is less than 5.
<EnteredInteger> is equal to 5.
<EnteredInteger> is greater than 5.


Only output one of the messages above if the number was in the range 0 to 10.



If the number was outside of the range 0 to 10 then display the following message:
Sorry <FirstName>, I needed a number between 0 and 10. Please run the program again.



Examples


Please enter your first name: dave
Dave, please enter an integer between 0 and 10 inclusively: 5
Entered number 5 is in range
5 is equal to 5.

Please enter your first name: dave
Dave, please enter an integer between 0 and 10 inclusively: 20
Sorry Dave, I needed a number between 0 and 10. Please run the program again.

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "{}, please enter an integer between {} and {} inclusively: "
# "Entered number {} is in range"
# "{} is less than {}."
# "{} is equal to {}."
# "{} is greater than {}."
# "Sorry {}, I needed a number between {} and {}. Please run the program again."

min_range = 0
max_range = 10

first_name = input("Please enter your first name: ").capitalize()
integer = int(input("{}, please enter an integer between {} and {} inclusively: ".format(first_name, min_range,
                                                                                         max_range)))
valid_range = range(0, 11)

if integer in valid_range:

    five = 5
    less_than_5 = integer < 5
    equal_to_5 = integer == 5
    greater_than_5 = integer > 5
    x = "Entered number {} is in range".format(integer)
    # Nice variable but..
    if less_than_5:
        print(x)
        print("{} is less than {}.".format(integer, five))
    elif equal_to_5:
        print(x)
        print("{} is equal to {}.".format(integer, five))
    else:
        print(x)
        print("{} is greater than {}.".format(integer, five))
else:   # No xxx rated here, hehehe.
    print("Sorry {}, I needed a number between {} and {}. Please run the program again.".format(first_name, min_range,
                                                                                                max_range))
