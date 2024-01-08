#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
last_didgit_txt = ""
if last_digit > 5:
    last_digit_txt = " and is greater than 5"
elif last_digit == 0:
    last_digit_txt = " and is 0"
else:
    last_digit_txt = " and is less than 6 and not 0" 
print("Last digit is " + str(number) + " is " + str(last_digit) + last_digit_txt)
