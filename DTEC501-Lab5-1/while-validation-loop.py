number1 = int(input("Enter your number: "))
while number1 not in (0,1):
    print("You must enter a binary number.")
    number1 = int(input("Enter your number: "))

number2 = int(input("Enter your second number: "))
while number2 not in (0,1):
    print("You must enter a binary number")
    number2 = int(input("Enter your second number: "))

print(number1, number2)