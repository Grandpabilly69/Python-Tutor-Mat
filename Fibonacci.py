num = int(input("Enter a number: "))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1


    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(num))


num1 = 0
num2 = 1
next_number = num1
count = 1

while count <= num:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()