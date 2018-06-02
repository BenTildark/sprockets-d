"""
Write a program which asks the user a few questions and works out if they can go to the beach and buy an ice cream.

The user can go to the beach if the current temperature is greater than or equal to 20 degrees.

The user may or may not have cash in their pocket. The amount of money they have will have a fractional component e.g.
$3.50.  This will be a float (floating point value).  For $3.50, they can enter 3.5 or 3.50

The cost of an ice cream will have a fractional component e.g. $2.50. This will be a float. For $2.50,
they can enter 2.5 or 2.50

The temperature is an integer.

If it is warm enough to go to the beach and the user has enough cash, then they can buy an ice cream.



Your program must display the following message:

Please enter your first name:

The user will enter their <FirstName> at this point.



The program should then output the following message

Hi <FirstName>, please tell me how hot it is now:

The user will enter the temperature at this point.



If it is warm enough, do the following:

                Display the message:

                You can go to the beach because it is <TheTemperature> degrees.



                Ask the user to enter how much cash they have in their pocket. Display the following message:

                Please tell me how much cash you have:

                The user will enter <AvailableCash> at this point.



                If they have cash in their pocket (they entered value > 0), do the following:

                                Ask the user to enter the cost of an ice cream.  Display the following message:

                                How much is an ice cream?

                                The user will enter <IceCreamCost> at this point.



                                If the user has enough money for an ice cream, do the following:

                                                                Work out how much money they will have left after buying the ice cream.

                                                                Display the message:

                                                                You can buy an ice cream and you will have <RemainingMoney> left.



                                If the user does not have enough money for an ice cream, display the message

                                     Sorry, no ice cream today.



                If they didn't have any cash in their pocket, display the message

                     Please remember to bring cash next time.



If it is not warm enough, display the message

        It's not warm enough, stay at home.



Just look at all that pesudo-ish pseudo code!



Examples


Please enter your first name: dave
Hi Dave, please tell me how hot it is now: 10
It's not warm enough, stay at home.

Please enter your first name: dave
Hi Dave, please tell me how hot it is now: 21
You can go to the beach because it is 21 degrees.
Please tell me how much cash you have: 10
How much is an ice cream? 3
You can buy an ice cream and you will have $7.00 left.

"""

# Auth: Michael Devenport.

# The Big Day Out ~ BLTN..

name_prompt = "Please enter your first name: "
potato = "Hi {}, please tell me how hot it is now: "
bdo = "You can go to the beach because it is {} degrees."
cash_query = "Please tell me how much cash you have: "
cost_query = "How much is an ice cream? "
transaction_success = "You can buy an ice cream and you will have ${:.2f} left."
transaction_failure = "Sorry, no ice cream today."
nil_funds_prompt = "Please remember to bring cash next time."
to_cold = "It's not warm enough, stay at home."

twenty_degree = 20
nil_funds = 0

first_name = input(name_prompt).capitalize()
celsius = int(input(potato.format(first_name)))  # Hopefully its a hot one..

if celsius >= twenty_degree:
    print(bdo.format(celsius))

    cash_total = float(input(cash_query))
    if cash_total > nil_funds:
        cost = float(input(cost_query))
        # I like this a lot!! I just thought I'd try assign change to bal
        # because bal was not readable for transaction success formatting.
        change = bal = cash_total - cost  # assigning the assignment all on 1 line, neat!
        if bal >= nil_funds:
            print(transaction_success.format(change))
        else:
            print(transaction_failure)

    else:
        print(nil_funds_prompt)
else:
    print(to_cold)
