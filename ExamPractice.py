#Question 1
from operator import contains


def km_to_miles(km):
    return (km * 0.62)

km = float(input("Enter the km: "))

print(km_to_miles(km))

#question 2

def is_divi(x):
    if x % 11 == 0:
        return True
    else:
        return False

x = int(input("Enter the number: "))
print(is_divi(x))

#Quesion3

def num(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Same"

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

print(num(a,b))

#Question 4

import math

def hex_area(side):
    area = 3 * math.sqrt(3)
    area = area / 2
    area = area * (side**2)
    return area

side = float(input("Enter the side: "))

print(hex_area(side))


#Question 5

def palindrome(x):
    temp = x[::-1]
    if temp == x:
        return True
    else:
        return False

x = input("Enter the word: ")

print(palindrome(x))

#Question 6

def fuelcost(mpl, cost):
    return mpl * cost

mpl = (input("Enter the mpl: "))
cost = (input("Enter the cost: "))

try:
    mpl = int(mpl)

except ValueError:
    mpl = 50

try:
    cost = int(cost)
except ValueError:
    cost = 1


print(fuelcost(mpl,cost))

# Question 7

def prime(num):

    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


#Question 8

def primenums(num):
    lst = []
    for i in range(2, num+1):
        bcheck = True
        for j in range(2, i):
            if i % j == 0:
                bcheck = False

        if bcheck == True:
            lst.append(i)

    return lst

num = int(input("Enter the number: "))

print(primenums(num))

#Question 9

def hcf(a,b):
    hh = 0
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            hh = i
    return hh

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

print(hcf(a,b))


#question 10

def email(x):
    bat = False
    if len(x)>256:
        return "Too long"
    for i in range(x):
        if x[0] == "@":
            return "No letters before @"

        if x[i] == "@":
            bat = True
            if x[i+1] == ".":
                return "No letter inbetween @ and ."

        if x[i] == ".":
            if x[i+1] == "":
                return "No letters after ."

    if bat == False:
        return "no @ symbol"




alphabet = "abcdefghijklmnopqrstuvwxyz"
