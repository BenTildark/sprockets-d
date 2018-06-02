"""
Write a program which asks the user to enter the start and end values for two nested loops.

Use for loops for this task.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter the start value for the inner loop:

Please enter the end value for the inner loop:

Please enter the start value for the outer loop:

Please enter the end value for the outer loop:

Display the loop counters each time you go around the loop as <Outer><Space><Inner>

Hint.  A nested loop is needed for this question.

Example

Please enter your first name: dave
Hi Dave, please enter the start value for the inner loop: 1
Please enter the end value for the inner loop: 3
Please enter the start value for the outer loop: 1
Please enter the end value for the outer loop: 2
1 1
1 2
1 3
2 1
2 2
2 3

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.

name_str = "Please enter your first name: "
inner_start_str = "Hi {}, please enter the start value for the inner loop: "
inner_end_str = "Please enter the end value for the inner loop: "
outer_start_str = "Please enter the start value for the outer loop: "
outer_end_str = "Please enter the end value for the outer loop: "
counter_str = "{} {}"

first_name = input(name_str)

inner_start_val = int(input(inner_start_str.format(first_name.capitalize())))
inner_end_val = int(input(inner_end_str))

outer_start_val = int(input(outer_start_str))
outer_end_val = int(input(outer_end_str))

inner_range = range(inner_start_val, inner_end_val+1)

outer_range = range(outer_start_val, outer_end_val+1)

for outer_range_count in outer_range:
    for inner_range_count in inner_range:
        print(counter_str.format(outer_range_count, inner_range_count))