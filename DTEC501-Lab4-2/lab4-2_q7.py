"""
After the users had been using your code for Lab4-2Q6, they reported there are a few issues and so they would like the code to be modified.

The grammar displayed is incorrect if the user enters 1 for their age.  Your solution needs to be aware of the use of singular and plural.
The code did not do any validation of the data as it was possible to enter negative years as the age and birth years that are in the future.


Use the code you wrote for Lab4-2Q6 as the basis for this question.

Write a program which asks the user to enter their first name followed by their age and the year in which they were born.

The program then works out if the age and birth year are correct based on the current year.

The program should ask the user to enter their first name

Please enter your first name:

then ask them to enter their age in years

Hi <FirstName>, please enter your age in years:

Treat the age as an integer.  A invalid age is a negative integer. 0 years is a valid age.

If the age is invalid display the message

<Age> is not a valid age.

and exit or stop running the program.



If the age is valid then ask the user to enter the year they were born in

Thank you. Please enter the year in which you were born:

If the year they say they were born is not valid (it is in the future) then display the message

Ah, a time traveller!


If the year they were born is valid then work out if the birth year is correct based on the entered age current year. If the entered age and year were correct, display the appropriate message from below

<FirstName>, based on you being <Age> year old, I agree, you were born in <BirthYear>.

<FirstName>, based on you being <Age> years old, I agree, you were born in <BirthYear>.

The message used above must be grammatically correct for the age.



If the entered age and year were not correct, display the grammatically correct message from below

<FirstName>, based on you being <Age> year old, you were not born in <BirthYear>.

<FirstName>, based on you being <Age> years old, you were not born in <BirthYear>.

followed by

You were actually born in <CorrectBirthYear>.



where <Age> and <BirthYear> are the values the user entered and <CorrectBirthYear> is the computed value based on the current year.

"""
# Auth: Michael Devenport.
# Email: croxleyway@gmail.com

# I didn't read the requirements thoroughly, missed 0 is valid age! ;-(

import time

current_year = time.strftime("%Y")

name_prompt = "Please enter your first name: "
age_prompt = "Hi {}, please enter your age in years: "
yob_prompt = "Thank you. Please enter the year in which you were born: "
return_true_prompt = "{}, based on you being {} {} old, I agree you were born in {}."
return_false_prompt = "{}, based on you being {} {} old, you were not born in {}."
return_correction_prompt = "You were actually born in {}."

dr_who = "Ah, a time traveller!"
age_error = "{} is not a valid age."
singular = "year"
to_plural = singular + "s"

first_name = input(name_prompt).capitalize()

age = int(input(age_prompt.format(first_name)))

if age >= 0:
    year_of_birth = int(input(yob_prompt))
    if year_of_birth == int(current_year) - age:
        if age == 1 and year_of_birth <= int(current_year):
            print(return_true_prompt.format(first_name, age, singular, year_of_birth))
        else:
            print(return_true_prompt.format(first_name, age, to_plural, year_of_birth))
    else:
        if age == 1 and year_of_birth <= int(current_year):
            print(return_false_prompt.format(first_name, age, singular, year_of_birth))
        elif year_of_birth > int(current_year):
            print(dr_who)
            exit()
        else:
            print(return_false_prompt.format(first_name, age, to_plural, year_of_birth))
        eval_yob = int(current_year) - age
        print(return_correction_prompt.format(eval_yob))
else:
    print(age_error.format(age))