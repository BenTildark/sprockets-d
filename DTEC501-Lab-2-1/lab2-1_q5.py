# Handling errors 5

"""
We are not conducting an evaluation, if we wanted to do comparision course_code & the string DTEC501 we could
but, first we would have to assign another dup "course_code" at lest then "course_code" would be defined & equal
to our string DTEC501. It would work fine BUT its verbose & the correct & "dry" solution is to simply change the
comparision state to a variable assigning the string.

"""

course_code = "DTEC501"
print(course_code)
