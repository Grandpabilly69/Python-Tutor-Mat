#Question 1
from math import trunc


def area(l,b):
    return l*b
length = int(input("Enter the length of sides: "))
bredth = int(input("Enter the bredth of sides: "))
print(area(length,bredth))

#Question 2

import random

def rnd():
    return random.randint(1,201)

rand = rnd()
if rand > 100:
    print("greater than 100")
elif rand < 100:
    print("less than 100")
else:
    print("equal")

#Question 3

import math

def pythag(a, b):

    return math.sqrt(a**2 + b**2)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print((pythag(a,b)))

#Question 4

def largerst(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print("{} is the largest number".format(largerst(a,b,c)))

#Question 5

def vowels(phrase):
    count = 0
    for i in phrase:
        if i in 'aeiouAEIOU':
            count += 1
    print(count)

phrase = str(input("Enter the phrase: "))

(vowels(phrase))