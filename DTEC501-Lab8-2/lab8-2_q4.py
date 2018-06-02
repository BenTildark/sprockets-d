"""
Modify your solution for Lab8-2 Q3 and allow the user to keep running the morse program until they indicate
they want to stop using it.

The stop phrase is St0P.  For clarification, spelt out in full that is

upper S lower t zero upper P full stop

If the stop phrase St0P. is entered, display the message

Thanks for practicing morse code.

and finish or stop running the program.

The specifications in Q3 still apply.

Hints.

Test for the stop phrase before converting the phrase to upper case.
The code requires a nested loop, one while and one for.

Example
Please enter the phrase to send: This is morse
T in morse is -
H in morse is ....
I in morse is ..
S in morse is ...
Gap
I in morse is ..
S in morse is ...
Gap
M in morse is --
O in morse is ---
R in morse is .-.
S in morse is ...
E in morse is .
Please enter the phrase to send: St0P.
Thanks for practicing morse code.

Example
Please enter the phrase to send: Not present!
N in morse is -.
O in morse is ---
T in morse is -
Gap
P in morse is .--.
R in morse is .-.
E in morse is .
S in morse is ...
E in morse is .
N in morse is -.
T in morse is -
! is not available in morse.
Please enter the phrase to send: Present
P in morse is .--.
R in morse is .-.
E in morse is .
S in morse is ...
E in morse is .
N in morse is -.
T in morse is -
Please enter the phrase to send: st0P.
S in morse is ...
T in morse is -
0 in morse is -----
P in morse is .--.
. in morse is .-.-.-
Please enter the phrase to send: St0p.
S in morse is ...
T in morse is -
0 in morse is -----
P in morse is .--.
. in morse is .-.-.-
Please enter the phrase to send: St0P.
Thanks for practicing morse code.
"""

# Written on: April 19 2018
# Developed by: Michael Devenport
# Email: croxleyway@gmail.com

# Lab8-2 Q4

# Primary loop assignment
still_practicing = True

# Exit assignment
exit_process = "St0P."

# Assign prompt/return strings outside of primary logic
phrase_prompt = "Please enter the phrase to send: "
return_morse_success = "{} in morse is {}"
whitespace_replacement = "Gap"
return_undefined_morse = "{} is not available in morse."
return_exit = "Thanks for practicing morse code."

# Morse code unit 'dict'
morse_code_units = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--"
}

# Implement loop while condition True
while still_practicing:

    phrase = input(phrase_prompt)

    if phrase == exit_process:    # 1. Evaluates True if phrase is equal to exit_process('St0P.')
        print(return_exit)        # With closing statement,
        still_practicing = False  # exit process.
    else:                         # Execute nested for loop iteration block( appending code ) if '1.' returns False
        for unit_key in phrase:
            unit_key = unit_key.upper()
            # Pass multiple values, in chained conditional argument, in single call to print function;
            # print <.> if condition True else print <..> if condition True else print <...>
            print(
                return_morse_success.format(unit_key, morse_code_units[unit_key]) if unit_key in morse_code_units
                else whitespace_replacement if unit_key.isspace()
                else return_undefined_morse.format(unit_key)
            )
