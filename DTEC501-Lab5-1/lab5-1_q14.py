"""
Write a program which asks the user to enter the start and end values for two nested loops.

Use while loops for this task.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter the start value for the inner loop:

Please enter the end value for the inner loop:

Please enter the start value for the outer loop:

Please enter the end value for the outer loop:



Display the loop counters each time you go around the loop as <Outer><Space><Inner>



Example


Please enter your first name: dave
Hi Dave, please enter the start value for the inner loop: 1
Please enter the end value for the inner loop: 4
Please enter the start value for the outer loop: 1
Please enter the end value for the outer loop: 3
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the start value for the inner loop: "
# "Please enter the end value for the inner loop: "
# "Please enter the start value for the outer loop: "
# "Please enter the end value for the outer loop: "
# "{} {}"

name_str = "Please enter your first name: "
inner_start_str = "Hi {}, please enter the start value for the inner loop: "
inner_end_str = "Please enter the end value for the inner loop: "
outer_start_str = "Please enter the start value for the outer loop: "
outer_end_str = "Please enter the end value for the outer loop: "
counter_str = "{} {}"

first_name = input(name_str)

inner_start_input = int(input(inner_start_str.format(first_name.capitalize())))
inner_end_input = int(input(inner_end_str))

outer_start_input = int(input(outer_start_str))
outer_end_input = int(input(outer_end_str))

inner_start_val = inner_start_input - 1
outer_start_val = outer_start_input - 1


while outer_start_val < outer_end_input:
    outer_start_val += 1
    while inner_start_val < inner_end_input:
        inner_start_val += 1
        print(counter_str.format(outer_start_val, inner_start_val))
    if inner_start_val == inner_end_input:
        inner_start_val = inner_start_input - 1