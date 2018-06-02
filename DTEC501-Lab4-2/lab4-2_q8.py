"""
DTEC123 (a fictitious course) has the following grades

Grade	Total marks
Distinction	90 and above
Merit	70-89
Pass	50-69
Fail	less than 50

There are 2 assessments for this course.

Assessment 1 has a minimum of 0 and a maximum of 50 marks and is worth 50% of the overall score.
Assessment 2 has a minimum of 0 and a maximum of 50 marks and is worth 50% of the overall score.

No partial marks are available for any question in either assessment.

Write a program which will do the following:

Ask the user for their first name.
Ask the user for their last name.
Ask the user for their assessment 1 mark.
Ask the user for their assessment 2 mark.

Based on the scores entered, display the resulting grade.

Do this by displaying the following messages:

Please enter your first name:
The user will enter their first name at this point.

<FirstName>, please enter your last name:
The user will enter their last name at this point.

<FirstName>, please enter your mark for assessment 1:
The user will enter their mark for assessment 1 at this point.

<FirstName>, please enter your mark for assessment 2:
The user will enter their mark for assessment 2 at this point.


If either of the assessment marks are out of range, display the message:
Sorry <FirstName>, one of your marks was out of range. Please re-run the program.

and stop running the program.

If the marks for both assessments are in range, calculate the overall mark for the course and look up the grade.

If the resulting grade is a Pass, Merit or Distinction then display the following message:
Congratulations <FirstName <LastName>, you have passed DTEC123 with a <Grade> grade.

If the grade is a Fail then display the following message:
Unfortunately <FirstName> <LastName>, you have not passed DTEC123.

where
<Grade> is Pass, Merit or Distinction.
<FirstName> is the users first name that they entered.
<LastName> is the users last name that they entered.
============================================================================
Examples:

Please enter your first name: got
Got, please enter your last/family name: pass
Got, please enter your mark for assessment 1: 26
Got, please enter your mark for assessment 2: 26
Congratulations Got Pass, you have passed DTEC123 with a Pass grade.



Please enter your first name: got
Got, please enter your last/family name: merit
Got, please enter your mark for assessment 1: 36
Got, please enter your mark for assessment 2: 36
Congratulations Got Merit, you have passed DTEC123 with a Merit grade.



Please enter your first name: not
Not, please enter your last/family name: passed
Not, please enter your mark for assessment 1: 10
Not, please enter your mark for assessment 2: 10
Unfortunately Not Passed, you have not passed DTEC123.



There are more than 10 test cases being tested by Moodle, only three possibilities are shown above.
You have to decide how to thoroughly test your code.  Think of the possible key combinations and test them.
Look at using values that are close to the boundaries of the grades mentioned in the question.

"""
# Auth: Michael Devenport.
# Email: croxleyway@gmail.com

course_code = "DTEC123"

distinction = range(90, 101)
merit = range(70, 90)
pass_course = range(50, 70)
fail_course = range(0, 51)

a_plus_grade = "Distinction"
a_grade = "Merit"
low_pass_grade = "Pass"

first_name_prompt = "Please enter your first name: "
last_name_prompt = "{}, please enter your last name: "
assessment_1_prompt = "{}, please enter your mark for assessment 1: "
assessment_2_prompt = "{}, please enter your mark for assessment 2: "
out_of_range_prompt = "Sorry {}, one of your marks was out of range. Please re-run the program."
pass_prompt = "Congratulations {} {}, you have passed {} with a {} grade."
failure_prompt = "Unfortunately {} {}, you have not passed {}."

first_name = input(first_name_prompt).capitalize()
last_name = input(last_name_prompt.format(first_name)).capitalize()

assessment_1_mark = int(input(assessment_1_prompt.format(first_name)))
assessment_2_mark = int(input(assessment_2_prompt.format(first_name)))

if all([assessment_1_mark >= 0, assessment_1_mark <= 50, assessment_2_mark >= 0, assessment_2_mark <= 50]):
    total_mark = assessment_1_mark + assessment_2_mark
    if total_mark in distinction:
        print(pass_prompt.format(first_name, last_name, course_code, a_plus_grade))
    elif total_mark in merit:
        print(pass_prompt.format(first_name, last_name, course_code, a_grade))
    elif total_mark in pass_course:
        print(pass_prompt.format(first_name, last_name, course_code, low_pass_grade))
    else:
        print(failure_prompt.format(first_name, last_name, course_code))
else:
    print(out_of_range_prompt.format(first_name))