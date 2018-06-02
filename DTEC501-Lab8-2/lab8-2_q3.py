"""
Using the pre-formatted dictionary key-value pairs below,
create a program which asks the user to enter a phrase and display
the morse code for each character in the entered phrase.

If the character is a space, indicate that there should be a gap by displaying

Gap

If the character is not in the dictionary, display

<chr> is not available in morse.

The given dictionary is not a full implementation of the ITU morse standard but is a cut down version.
Please use the version that is given.

Hint

The best loop to use is a for loop.  See slide 15 of Presentation 5-1.

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

"""

# Written on: April 18 2018
# Developed by: Michael Devenport
# Email: croxleyway@gmail.com

# Lab8-2 Q3

phrase_prompt = "Please enter the phrase to send: "
return_morse_success = "{} in morse is {}"
whitespace_replacement = "Gap"
return_undefined_morse = "{} is not available in morse."

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

phrase = input(phrase_prompt).upper()

# Iterate 'mutable' variable, setting temp object 'unit_key'as assignment of each char in each iteration.
# Implement a multi Ternary condition equivalent( do thing & return if condition True else do other thing & return
# if condition True else do thing & return. )

for unit_key in phrase:
    print(return_morse_success.format(unit_key, morse_code_units[unit_key]))\
        if unit_key in morse_code_units\
        else print(whitespace_replacement) if unit_key.isspace()\
        else print(return_undefined_morse.format(unit_key))
