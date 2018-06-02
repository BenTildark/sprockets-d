"""
Write a program which asks the user to enter their first name and a number between 0 and 10 inclusively.

Ask the user to enter their first name.

Please enter your first name:

The user will enter their <FirstName> at this point.

The program should output the following message
Hi <FirstName>, please enter a number between 0 and 10 inclusively:

The user will enter an integer <TheNumber> at this point.

The program should then test to see if the number is in the range 0 to 10 inclusively.
If  <TheNumber> is in that range then test to see which range it is in and display the appropriate message from the
following:

<TheNumber> is less than 3.
<TheNumber> is between 3 and 5 inclusively.
<TheNumber> is between 6 and 8 inclusively.
<TheNumber> is greater than 8.

Only output one of the messages above if the number was in the range 0 to 10 inclusively.

If the number was outside of the range 0 to 10 then display the following message:
Sorry <FirstName>, I needed a number between 0 and 10. Please run the program again.

Examples

Please enter your first name: zero
Hi Zero, please enter a number between 0 and 10 inclusively: 0
0 is less than 3.


Please enter your first name: three
Hi Three, please enter a number between 0 and 10 inclusively: 3
3 is between 3 and 5 inclusively.


Please enter your first name: four
Hi Four, please enter a number between 0 and 10 inclusively: 4
4 is between 3 and 5 inclusively.


Please enter your first name: five
Hi Five, please enter a number between 0 and 10 inclusively: 5
5 is between 3 and 5 inclusively.


Please enter your first name: six
Hi Six, please enter a number between 0 and 10 inclusively: 6
6 is between 6 and 8 inclusively.

Please consider the other combinations, there are more.

"""

# Auth: Michael Devenport.

# Initially developed this program with an 'int' input field but found it ran
# "ValueError: invalid literal for int() with base 10" if one entered a fractional number ie: 9.5 is between 0 - 10
# I added more complexity to the elvaluation by changing the int input to float,
# we can now evaluate any value within requirement, & hopefully still get by Moodle.

name_prompt = "Please enter your first name: "
num_prompt = "Hi {}, please enter a number between {} and {} inclusively: "
less = "{} is less than {}."
between = "{} is between {} and {} inclusively."
greater = "{} is greater than {}."
error = "Sorry {}, I needed a number between {} and {}. Please run the program again."

first_name = input(name_prompt).capitalize()
num = float(input(num_prompt.format(first_name, 0, 10)))

if all([num >= 0, num <= 10]):
    if num < 3:
        if str(num).endswith('.0'):
            print(less.format(int(num), 3))
        else:
            print(less.format(num, 3))
    elif all([num >= 3, num <= 5]):
        if str(num).endswith('.0'):
            print(between.format(int(num), 3, 5))
        else:
            print(between.format(num, 3, 5))
    elif all([num >= 6, num <= 8]):
        if str(num).endswith('.0'):
            print(between.format(int(num), 6, 8))
        else:
            print(between.format(num, 6, 8))
    else:
        if str(num).endswith('.0'):
            print(greater.format(int(num), 8))
        else:
            print(greater.format(num, 8))
else:
    print(error.format(first_name, 0, 10))
