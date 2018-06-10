# Random number game
# Assessment 2 code

import random

minimum_random_value = 1
maximum_random_value = 64
maximum_attempts = 6
guessed_correctly = False
number_of_guesses = 0
guesses = []

random_number = random.randint(minimum_random_value, maximum_random_value)
# Next line is for debugging.
print("random_number is {}.".format(random_number))

print("I've thought of a random number between {} and {}.".format(minimum_random_value, maximum_random_value))
print("You have {} attempts to try to guess the number.".format(maximum_attempts))

while (not (guessed_correctly) and (number_of_guesses != maximum_attempts)):
    guessed_number = int(input("Enter your guess: "))

    guesses.append(guessed_number)
    number_of_guesses = len(guesses)

    if (guessed_number < random_number):
        print("{} was too small".format(guessed_number))

    elif (guessed_number > random_number):
        print("{} was too big".format(guessed_number))

    else:
        print("Well done! {} is the correct answer.".format(guessed_number))
        guessed_correctly = True

if (not (guessed_correctly)):
    print("Sorry but you have used all your attempts.")
    print("The number I thought of was {}.".format(random_number))
