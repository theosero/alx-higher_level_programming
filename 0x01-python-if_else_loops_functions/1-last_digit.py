#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10

print("Last digit of {} is {} ".format(number, last_digit),end="")

if last_digit > 5:
    print("and is greater than {}".format(5))
elif last_digit == 0:
    print("and is {}".format(0))
elif last_digit < 6 and last_digit != 0:
    print("and is less than {} and not {}".format(6,0))
