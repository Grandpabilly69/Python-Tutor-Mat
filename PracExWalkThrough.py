def addup(lst):
    total = 0
    for i in lst:
        total += i
    return total

def times(lst):
    total = 1
    for i in lst:
        total *= i
    return total

length = int(input("Enter the length of the list: "))
lst2 = []
for i in range(length):
    temp = int(input("Enter the number: "))
    lst2.append(temp)

print(addup(lst2))
print(times(lst2))

#Next question

def reverse(phrase):
    temp = ""
    for i in phrase:
        temp = i + temp
    return temp

ph = input("Enter the phrase to be reversed: ")
print(reverse(ph))


#enwesgf

def func1(lst):
    for i in lst:
        print(i)

lst1 = []

for i in range(5):
    temp = int(input("Enter the number: "))
    lst1.append(temp)
func1(lst1)

#############################

def calculation(a, b):
    plus = a + b
    minus =  a-b

    return plus, minus

res = calculation(40, 10)
print(res)



##################################

def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False


    return True

print(prime(31))