"""
Write a program which asks the user to enter their first name, start, stop and increment values for the loop.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter the start value:

Thank you <FirstName>, please enter the end value:

Please enter the increment:

If the start and end values are valid based on the increment, use a while loop to loop from the start to the end in steps specified by the increment.

Display the following each time you go around the loop.

Line x

where x is the loop counter

If the start and end values are not valid based on the increment, display the following error message:

Sorry, I can't count from <Start> to <End> using an increment of <Increment>.

Examples

Please enter your first name: dave
Hi Dave, please enter the start value: 1
Thank you Dave, please enter the end value: 11
Please enter the increment: 2
Line 1
Line 3
Line 5
Line 7
Line 9
Line 11


Please enter your first name: dave
Hi Dave, please enter the start value: 10
Thank you Dave, please enter the end value: 1
Please enter the increment: 2
Sorry, I can't count from 10 to 1 using an increment of 2.


Please enter your first name: dave
Hi Dave, please enter the start value: 10
Thank you Dave, please enter the end value: 1
Please enter the increment: -1
Line 10
Line 9
Line 8
Line 7
Line 6
Line 5
Line 4
Line 3
Line 2
Line 1

"""
# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the start value: "
# "Thank you {}, please enter the end value: "
# "Please enter the increment: "
# "Line {}"
# "Sorry, I can't count from {} to {} using an increment of {}."

first_name = input("Please enter your first name: ").capitalize()
first_value = int(input("Hi {}, please enter the start value: ".format(first_name)))
second_value = int(input("Thank you {}, please enter the end value: ".format(first_name)))
step_value = int(input("Please enter the increment: "))

end_inclusive = second_value + 1
double_first_value = first_value * 2
max_negative_step = first_value - double_first_value
count = 0

while first_value < end_inclusive and step_value > 0 and step_value <= second_value:
    count += 1
    print("Line {}".format(first_value))
    # first_value = first_value + step_value
    first_value += step_value


while first_value >= second_value and step_value < 0 and step_value >= max_negative_step:
    count += 1
    print("Line {}".format(first_value))
    # first_value = first_value + step_value
    first_value += step_value

if count <= 0:
    print("Sorry, I can't count from {} to {} using an increment of {}.".format(first_value, second_value, step_value))



