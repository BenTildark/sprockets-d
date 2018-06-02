"""
Write a program to ask the user to enter their first/given name.
Your program must display the following message


Please enter your first name:

Your program must then output the following:
Hi EnteredFirstName.

Please enter the first integer:


and once the user has entered the value, display the following message:


Please enter the second integer:

Divide the first integer by the second integer display the following message:


EnteredFirstName, the answer to FirstInteger divided by SecondInteger is Result

where EnteredFirstName is the users first name and FirstInteger and SecondInteger are the respective integers the user entered.
Result is the quotient of the two integers.



Example


Please enter your first name: Bill
Hi Bill.
Please enter the first integer: 10
Please enter the second integer: 2
Bill, the answer to 10 divided by 2 is 5.0

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi "
# "."
# "Please enter the first integer: "
# "Please enter the second integer: "
# ", the answer to "
# " divided by "
# " is "

"""
"""
Multi-line, Same-line Output division. DIVISION
"""

first_name = input("Please enter your first name: ").capitalize()
print("Hi ", first_name, ".", sep="", end="\n")

first_addend = int(input("Please enter the first integer: "))
second_addend = int(input("Please enter the second integer: "))

answer = first_addend / second_addend
print(first_name, ", the answer to ", first_addend, " divided by ", second_addend, " is ", answer, sep="", end="")



















