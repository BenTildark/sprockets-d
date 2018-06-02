"""
Write a program to ask the user to enter their first name.
Your program must display the following message:


Please enter your first name:

Your program must then display the following:


Hi EnteredFirstName.
Please enter the first integer:


and once the user has entered the value, the program must display the following message:


Please enter the second integer:

The user enters the second integer at this point.


Divide the first integer by the second integer display the following message:


EnteredFirstName, the answer to FirstInteger modulus SecondInteger is Result


where EnteredFirstName is the users first name and FirstInteger and SecondInteger are the respective integers the user entered.
Result is the modulus of the two integers.



Example


Please enter your first name: Marie
Hi Marie.
Please enter the first integer: 6
Please enter the second integer: 3
Marie, the answer to 6 modulus 3 is 0

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi "
# "."
# "Please enter the first integer: "
# "Please enter the second integer: "
# ", the answer to "
# " modulus "
# " is "

"""

"""
Multi-line, Same-line Output division. MODULUS
"""

first_name = input("Please enter your first name: ").capitalize()
print("Hi ", first_name, ".", sep="", end="\n")

first_addend = int(input("Please enter the first integer: "))
second_addend = int(input("Please enter the second integer: "))

answer = first_addend % second_addend
print(first_name, ", the answer to ", first_addend, " modulus ", second_addend, " is ", answer, sep="", end="")

















