"""
Write a program which asks the user to enter an integer by displaying the following message:

Please enter an integer:

Using an augmented assignment statement, increment the integer by one and display the following message:


The answer to EnteredInteger + 1 is Result.



where EnteredInteger is the value the user entered and Result is incremented value.



Example


Please enter an integer: 5
The answer to 5 + 1 is 6

"""

# The lines of text you need to use to generate the output are given below for you.
#   Do not alter anything inside the quotes.
# "Please enter an integer: "
# "The answer to {} + {} is {}"

addend = int(input("Please enter an integer: "))


def addition(arg):
    answer = arg + 1
    result = "The answer to {} + {} is {}".format(arg, 1, answer)
    print(result)


addition(addend)
