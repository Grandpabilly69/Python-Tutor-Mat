#Question 2

# x = 43
# x = x +1
# print(x)

# mins = 60
# day = 24
#
# total = mins * day
# print(total)

# print("5" * 3)
#
# x = 50 * 2 + (60 -20) /4
#
# print(x)

# x = "12345"
#
# print(x[2] + x[1] + x[0] + x[3] + x[4])
#
# word = "happiness"
# print(len(word[1:4]))

# def func(x):
#     return x+1
#
# f = func
#
# print(f(2) + func(2))

#Question 3
#
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
#
# if x == y:
#     print("The numbers are equal")
# else:
#     if x<y:
#         print("The numbers are less than the numbers")
#     else:
#         print("dgfgshf")

#Question 4

# far = int(input("Enter temp in farenheight: "))
# clesius = (far - 32) * 5 / 9
#
# print("the temp is {:.2f}".format(clesius))

#Question 5
#
# weather = input("is it raining outside(yes/no): ").lower()
#
# if weather == "yes":
#     print("take an umbrella")
# else:
#     print("not valid")
#
# print("leave the house")

#Question 6

length = float(input("Enter the total trail kms: "))
cycles = float(input("Enter the kms cycled a day: "))
days = int(input("Enter the number of days: "))

km = length - (cycles*days)

print("you have {:.2f}kms left".format(km))