deincrement_operand = start_value # - 1
increment_operand = start_value # + 1
end_operand = end_value + 2

count = 0 # Here's a trick!

while deincrement_operand < end_value and inc_value > 0 and inc_value != 0 and end_value >= inc_value:

    if deincrement_operand <= end_operand:
        count += 1 # increment count only if this block run
        print("Line {}".format(deincrement_operand))
        deincrement_operand += inc_value


while increment_operand >= end_operand and inc_value < 1 and inc_value != 0:
    increment_operand += inc_value   # Here's another trick! We need to increment the 'increment_operand' by the neg inc_value
                                     # in order to decrease increment_operand. OMG!
    if increment_operand >= end_value:
        count += 1 # increment count only if this block run
        print("Line {}".format(increment_operand))

if count <= 0: # Check if No "while condition were True"
    print("Sorry, I can't count from {} to {} using an increment of {}.".format(start_value, end_value, inc_value))
