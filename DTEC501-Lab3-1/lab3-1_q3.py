"""
Write a program to ask the user to enter their first name.
Your program must display the following message:
Please enter your first name:


Your program must then output the following:
Hi EnteredFirstName, please enter the first integer:


and once they have entered it, display the following message:
Please enter the second integer:

Multiply the first integer by the second integer display the following message:


EnteredFirstName, the answer to FirstInteger * SecondInteger is Result


where EnteredFirstName is the users first name and FirstInteger and SecondInteger are the respective integers the user entered. Result is the product of the two integers.



Example


Please enter your first name: Dave
Hi Dave, please enter the first integer: 3
Please enter the second integer: 4
Dave, the answer to 3 * 4 is 12

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the first integer: "
# "Please enter the second integer: "
# "{}, the answer to {} * {} is {}"

first_name = input("Please enter your first name: ")
first_addend = int(input("Hi {}, please enter the first integer: ".format(first_name)))
second_addend = int(input("Please enter the second integer: "))


def multiplication(first_arg, second_arg, third_arg):
    answer = second_arg * third_arg
    result = "{}, the answer to {} * {} is {}".format(first_arg, second_arg, third_arg, answer)
    print(result)


multiplication(first_name, first_addend, second_addend)