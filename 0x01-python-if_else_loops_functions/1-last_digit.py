#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = ""
string = "Last digit of " + str(number) + " is " 
if number < 0:
 last_digit = (-1)*((-1 * number) % 10)
else:
 last_digit = number % 10
if last_digit > 5:
 string = string + str(last_digit) +" and is greater than 5"
elif last_digit == 0:
 string = string + str(last_digit) + " and is 0"
else:
 string = string + str(last_digit) + " and is less than 6 and not 0"
print(string)
