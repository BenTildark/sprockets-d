"""
Modify the code you wrote for Lab11-2 Q2 and display the string returned by using the ShowInfo dialogue box,
not the console.


Example


If the value returned from the function is "Out of Toucan error." then using ShowInfo, set the window title to
"Toucan :-(" and the message to "Out of Toucan error."



If the value returned from the function is "No toucan do." then using ShowInfo, set the window title to "Toucan :-)"
and the message to "No toucan do.".

If the value returned from the function is "One Toucan, can't one?" then using ShowInfo, set the window title to
"Toucan :-)" and the message to "One Toucan, can't one?"

If the value returned from the function is "Toucan play at that game. then using ShowInfo, set the window title to
"Toucan :-)" and the message to "Toucan play at that game."

If the value returned from the function is "Toucan for sale." then using ShowInfo, set the window title to "Toucan :-)"
and the message to "Toucan for sale."

If the value returned from the function is "Toucan ate the pies." then using ShowInfo, set the window title to
"Toucan :-)" and the message to "Toucan ate the pies."

"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Q: lab 13-1 q1

from tkinter.messagebox import *


def can(param):

    """GUI display phrase if valid key is passed in else toucan error"""

    phrase = {
        '0': "No Toucan do.",
        '1': "One Toucan, can't one?",
        '2': "Toucan play at that game.",
        '4': "Toucan for sale.",
        '8': "Toucan ate the pies.",
        'n': "Toucan :-(",
        'y': "Toucan :-)",
        'error': "Out of Toucan error."
    }
    if str(param) in phrase:
        showinfo(title=phrase['y'], message=phrase[str(param)])

    else:
        showinfo(title=phrase['n'], message=phrase['error'])


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
