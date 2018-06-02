"""
Write a program which asks the user to enter their first name followed by their age and then display the year in which they were born.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter your age in years:

Treat the age as an integer.  A invalid age is a negative integer. 0 years is a valid age.

Work out which year the user was born in and display the appropriate message from below

<FirstName>, it is now <CurrentYear>, you are <Age> year old and so you were born in <YearOfBirth>.

<FirstName>, it is now <CurrentYear>, you are <Age> years old and so you were born in <YearOfBirth>.

The message used above must be grammatically correct for the age.

<FirstName> is the users first name.

<CurrentYear> is the current year

<Age> is the age in years of the user.

<YearOfBirth> is the year the user was born in.



if the entered age was invalid, display the message

<Age> is an invalid age.



Use a variable to represent the current year.



An ideal solution uses two if's and one else and has only one instance of the "<FirstName>, it is now <CurrentYear>, you are ... " line.



Examples


Please enter your first name: Jane
Hi Jane, please enter your age in years: 1
Jane, it is now 2018, you are 1 year old and so you were born in 2017.



Please enter your first name: TooYoung
Hi Tooyoung, please enter your age in years: -10
-10 is an invalid age.



Please enter your first name: Elaine
Hi Elaine, please enter your age in years: 22
Elaine, it is now 2018, you are 22 years old and so you were born in 1996.


"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter your age in years: "
# "{}, it is now {}, you are {} {} old and so you were born in {}."
# "{} is an invalid age."
# "year"
# "s"

first_name = input("Please enter your first name: ").capitalize()
age = int(input("Hi {}, please enter your age in years: ".format(first_name)))

current_year = 2018
invalid_age = age < 0
year_of_birth = current_year - age
years = "year" + "s"

if invalid_age:
    print("{} is an invalid age.".format(age))
elif age == 1:
    print("{}, it is now {}, you are {} {} old and so you were born in {}.".format(first_name, current_year, age,
                                                                                   "year", year_of_birth))
else:
    print("{}, it is now {}, you are {} {} old and so you were born in {}.".format(first_name, current_year, age,
                                                                                   years, year_of_birth))