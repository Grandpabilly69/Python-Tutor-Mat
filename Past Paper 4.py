i = int(3)

f = float(3)

print(i)
print(f)

#String

s = input("Enter a string: ")
print(s.upper())

phrase = "hello, world!"
print(phrase[7:12])

#For Loops
import math
def sum_of_squares(n):
    strong = 0
    for i in range(1, n+1):
        if (math.sqrt(i)).is_integer():
            strong += i
    return strong

p = int(input("Enter a number: "))
print(sum_of_squares(p))

#While loop

def countdown(n):
    while n >= 0:
        print(n)
        n -= 1

countdown(13)

#Random num

import random

rnd = random.randint(0,101)

print(rnd)

#Clause

lang = ["Java", "C++", "Python", "JavaScript"]
b = False
for i in lang:
    if i == "Python":
        b = True
        break
if b:
    print("Found")
else:
    print("Not Found")
