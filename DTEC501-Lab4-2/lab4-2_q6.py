"""
Write a program which asks the user to enter their first name followed by their age and the year in which they were born

The program then works out if the age and birth year are correct based on the current year.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter your age in years:

followed by

Thank you. Please enter the year in which you were born:

The program needs to work out if the age and birth year are correct based on the current year.
If the entered values were correct, display the following message:

<FirstName>, based on you being <Age> years old, I agree, you were born in <YearOfBirth>.

If the entered values were not correct, display the following messages:

<FirstName>, based on you being <Age> years old, you were not born in <YearOfBirth>.

You were actually born in <CorrectBirthYear>.

where <Age> and <YearOfBirth> are the values the user entered and <CorrectBirthYear> is the computed value
based on the current year.

Examples

Please enter your first/given name: dave
Hi Dave, please enter your age in years: 42
Thank you. Please enter the year in which you were born: 1976
Dave, based on you being 42 years old, I agree, you were born in 1976.

Please enter your first/given name: dave
Hi Dave, please enter your age in years: 41
Thank you. Please enter the year in which you were born: 1975
Dave, based on you being 41 years old, you were not born in 1975.
You were actually born in 1977.

"""
# Auth: Michael Devenport.

# Rather than hard code this year( assignment variable set to 2018 )
# I figure this is better approach, create a dynamic assignment set to current_year,
# that way it will work next year too.

# I've noticed this program is not absolutely true( as you clearly know ) without the month & day attributes of
# shall we say, our DOB object has nothing to evaluate against current month & day which we could get from time.
# Tech speaking this program could be out by 12 months plus if a person was 44 & born in 1973 who's birthday was 24/12.
# This could be the case & return an error/bug claiming the input is wrong ( you were actually born in 1974 )
# Guess you have a question in your arsenal that takes all DOB attributes into account.

import time

current_year = time.strftime("%Y")

name_prompt = "Please enter your first/given name: "
age_prompt = "Hi {}, please enter your age in years: "
yob_prompt = "Thank you. Please enter the year in which you were born: "
return_true_prompt = "{}, based on you being {} years old, I agree, you were born in {}."
return_false_prompt = "{}, based on you being {} years old, you were not born in {}."
return_correction_prompt = "You were actually born in {}."

first_name = input(name_prompt).capitalize()
age = int(input(age_prompt.format(first_name)))
year_of_birth = int(input(yob_prompt))

if year_of_birth == int(current_year) - age:  # refactored: evaluation & equation can be preformed on the same line.
    print(return_true_prompt.format(first_name, age, year_of_birth))
else:
    print(return_false_prompt.format(first_name, age, year_of_birth))
    eval_yob = int(current_year) - age
    print(return_correction_prompt.format(eval_yob))


