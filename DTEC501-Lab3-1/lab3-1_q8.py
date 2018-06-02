"""
Write a currency exchange application.

Ask the user to enter the current NZ to AU exchange rate and how much NZ money they will exchange and then display the equivalent in Australian dollars.

The application must ask the user to enter their name by displaying the following:

Please enter your first name:

Then ask the user to enter the exchange rate by displaying the following:

Hi FirstName. Please enter the NZ/AU exchange rate:

The first name must be correctly capitalised.

Ask the user to enter the amount they want to exchange by displaying the following:


Please enter the amount of NZ $'s you want to exchange:

Then display the following:


FirstName, I can exchange KiwiDollars NZD into AussieDollars AUD for you.
where FirstName is the first name the user entered, KiwiDollars is the value of the variable containing the amount the user wishes to exchange and AussieDollars is the value of the variable containing the equivalent in Australian $'s.



Examples


Please enter your first name: harry
Hi Harry. Please enter the NZ/AU exchange rate: 0.94
Please enter the amount of NZ $'s you want to exchange: 10
Harry,  I can exchange 10.00 NZD into 9.40 AUD for you.



Please enter your first name: BiLL
Hi Bill. Please enter the NZ/AU exchange rate: 0.94
Please enter the amount of NZ $'s you want to exchange: 1001.99
Bill, I can exchange 1001.99 NZD into 941.87 AUD for you.

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}. Please enter the NZ/AU exchange rate: "
# "Please enter the amount of NZ $'s you want to exchange: "
# "{}, I can exchange {:.2f} NZD into {:.2f} AUD for you."

"""
Expected output.

Please enter your first name: harry
Hi Harry. Please enter the NZ/AU exchange rate: 0.94
Please enter the amount of NZ $'s you want to exchange: 10
Harry,  I can exchange 10.00 NZD into 9.40 AUD for you.

Instruction & string components

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}. Please enter the NZ/AU exchange rate: "
# "Please enter the amount of NZ $'s you want to exchange: "
# "{}, I can exchange {:.2f} NZD into {:.2f} AUD for you."
"""
# NZD to AUD Currency Converter

first_name = input("Please enter your first name: ").capitalize()

exchange_rate = float(input("Hi {}. Please enter the NZ/AU exchange rate: ".format(first_name)))

nzd = int(input("Please enter the amount of NZ $'s you want to exchange: "))

aud = exchange_rate * nzd

print("{}, I can exchange {:.2f} NZD into {:.2f} AUD for you.".format(first_name, nzd, aud))