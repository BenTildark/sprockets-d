"""
Create a password changing program.  In order to have their password changed, the user must enter their password twice.
It is necessary to enter the password twice so that the user is sure they have entered the same password.
You are not actually changing passwords, merely checking strings.

Your code needs to call the validate_password function you created in Lab 14-1-2 (Q1).

Do *not* modify the validate_password function.

The validate_password function does *not* display the ShowInfo or ShowWarning dialogue message boxes.

The validate_password function returns a boolean value.  Use this boolean value to display
the appropriate dialogue message box.  This is the same concept you used for Assessment 2 Revision Lab 1 Q2 where
one function calls another which is the same concept you have been using for a while with your function where they
call the print() function.

Place the validate_password function inline with the code for this question.

================================
When the user clicks the change password button, you need to validate the entered password by calling the
validate_password function and passing it the passwords that have been entered.

If the validate_password returns True, use the ShowInfo dialogue message box to inform the user that the password
has been changed.

e.g.

If the validate_password returns False,  use the ShowWarning dialogue message box to inform the user that the
password has not been changed.

e.g.


"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com


from tkinter import *
# from function_module import validate_password
from tkinter.messagebox import *


def validate_password(first_pwd, second_pwd):

    """return True if valid password else False."""

    min_length = 8
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_vowels = 2
    min_char_by_type = 1

    if all([len(first_pwd) >= min_length, first_pwd == second_pwd]):
        count_vowel, count_upper, count_lower = 0, 0, 0
        for char in first_pwd:
            if char.lower() in vowels:
                count_vowel += 1
            if char.isupper():
                count_upper += 1
            if char.islower():
                count_lower += 1

        if not first_pwd[0].isnumeric():
            if all([count_vowel <= max_vowels, count_upper >= min_char_by_type, count_lower >= min_char_by_type,
                    first_pwd[0].lower() != first_pwd[-1].lower()]):
                return True
            else:
                return False
        elif all([count_vowel <= max_vowels, count_upper >= min_char_by_type, count_lower >= min_char_by_type]):
            return True
        else:
            return False

    else:
        return False


def run_check():
    validator = validate_password(entered_data1.get(), entered_data2.get())
    if validator:
        showinfo(None, "Your password has been changed.")
    else:
        showwarning(None, "Your password has not been changed.")


# Create root window
root = Tk()

# Set window size in pixels
root.geometry("260x230")

# Add label to root window
pwd_label = Label(root, text="Please enter your password")
pwd_label.pack()

# Add password fields
entered_data1 = StringVar()
pwd1 = Entry(root, show="*", textvariable=entered_data1)
pwd1.pack()
entered_data2 = StringVar()
pwd2 = Entry(root, show="*", textvariable=entered_data2)
pwd2.pack()

# Add submit button
pwd_btn = Button(None, text="Change password", command=run_check)
pwd_btn.pack()

root.mainloop()
