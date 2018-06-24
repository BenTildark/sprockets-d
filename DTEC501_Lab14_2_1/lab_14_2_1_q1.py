"""
Use the code you wrote for Lab14-1-3 as the basis for this question.

This question adds menus and different message boxes to the application.

As per  Lab14-1-3, your code needs to call the validate_password function you created in Lab14-1-2 (Q1).
You must not modify the code for the validate_password function, assuming you correctly answered Lab14-1-2,
then it needs to be left as is.


Ensure the window title can be seen without having to manually resize the window.

The application has menus.


Requirements
When the user clicks the check password button, you need to validate the entered password.
The function assigned to the check password button needs to pass both passwords to the validate_password function.

If the password is valid, display


If the password is not valid, display


After the user clicks the check password button, for security reasons the passwords that were entered must be
removed from the text areas.  Do this by calling the same function that is called by the File/Reset menu option.

If the user selects the File/Reset option from the menu, then remove (clear) both of the passwords from the text areas.

If the user selects the File/Exit option from the menu, then exit from the application.

If the user selects the Help/About option from the menu, then display the following dialogue.


The function you use to display the Help/About dialogue must receive the version number as a parameter.

Please do not use your actual password for testing the code.

"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Lab: 14_2_1 GUI Password checker with cascade menu


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
    reset_password()
    if validator:
        showinfo(None, "Your password meets the security standard.")
    else:
        showwarning(None, "Your password does not meet the security standard.")


def reset_password():
    """Reset pwd handler."""
    entered_data1.set('')
    entered_data2.set('')


def display_help_about():
    """ Display typical help about."""
    showinfo("Help about.", "Password checker version 1.1")


def exit_menu():
    """Tidy up and exit gracefully."""
    root.destroy()


# Create root window
root = Tk()
menubar = Menu(root)

# Set window title
root.title("Password validation")

# Set window size in pixels
root.geometry("260x230")

file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(label="Reset", command=reset_password)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_menu)

menubar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menubar, tearoff=0)

help_menu.add_command(label="About", command=display_help_about)
menubar.add_cascade(label="Help", menu=help_menu)

# Add first label
pwd_label1 = Label(root, text="Please enter your password")
pwd_label1.pack()
# Add first password field
entered_data1 = StringVar()
pwd1 = Entry(root, show="*", textvariable=entered_data1)
pwd1.pack()
# Add second label
pwd_label2 = Label(root, text="Please re-enter your password")
pwd_label2.pack()
# Add second password field
entered_data2 = StringVar()
pwd2 = Entry(root, show="*", textvariable=entered_data2)
pwd2.pack()

# Add submit button
pwd_btn = Button(None, text="Check password", command=run_check)
pwd_btn.pack()

root.config(menu=menubar)

root.mainloop()




