"""
The purpose of this lab is to troubleshoot existing code.

You can use the debugger if you want to but you don't have to.

You can use whatever debugging techniques you have been using so far if you prefer.

===================================================================================

The program is supposed to remove any leading and/or trailing spaces and correctly capitalise the entered name before printing it.
There are mistakes in the code.
Leave the text inside the print and input sections as they are.
Use debugging techniques to correct the code.



Code
first_name = input("Enter your first name: ")
first_name = first_name.capitalize()
first_name = first_name.strip()
print("[{}]".format(first_name))



Examples
Enter your first name: OneLeadingSpace
[Oneleadingspace]


Enter your first name: OneLeadingAndOneTrailingSpace
[Oneleadingandonetrailingspace]



"""

# Auth: Michael Devenport.
# Email: croxleyway@gmail.com

# The following code is supposed to
# remove any leading and/or trailing spaces and
# correctly capitalise the entered name before printing it.
# There are mistakes in the code.
# Leave the text inside the print and input sections as they are.
# Use debugging techniques to correct the code.

first_name = input("Enter your first name: ").strip().capitalize()
# first_name = first_name.capitalize()
# first_name = first_name.strip()
print("[{}]".format(first_name))

