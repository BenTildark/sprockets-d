"""
Write a function called can. can has 1 parameter and returns a string based on the value of the argument
that was passed.

The function does not generate any output.

The string that needs to be returned is shown in the answer section below.

The function must make use of a dictionary for storing the strings.

Hint.

Ideally, your solution will use 1 if and 1 else.

Example output
reqd_toucan = 0
print(can(reqd_toucan))
No Toucan do.

reqd_toucan = 1
print(can(reqd_toucan))
One Toucan, can't one?

reqd_toucan = 2
print(can(reqd_toucan))
Toucan play at that game.

reqd_toucan = 4
print(can(reqd_toucan))
Toucan for sale.

reqd_toucan = 8
print(can(reqd_toucan))
Toucan ate the pies.

If any other value is passed, return "Out of Toucan error."


reqd_toucan = 16
print(can(reqd_toucan))
Out of Toucan error.
"""
# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Q: lab 11-2 q2


def can(param):

    """return phrase if valid key is passed in else toucan error"""

    phrase = {
        '0': "No Toucan do.",
        '1': "One Toucan, can't one?",
        '2': "Toucan play at that game.",
        '4': "Toucan for sale.",
        '8': "Toucan ate the pies.",
        'error': "Out of Toucan error."
    }
    if str(param) in phrase:
        return phrase[str(param)]
    else:
        return phrase['error']


# return each key & phrase through iteration
ignore = [3, 5, 6, 7]
for i in range(0, 9):
    print(i)
    if i not in ignore:
        print(can(i))

print()

# return toucan error
print('5', can(5))
print('9', can(9))
