def prime():
    num = int(input("Enter a number: "))
    n = num-1
    while(n > 1):
        if num % n == 0:
            return("not prime")


        n = n -1
    return("prime")

print(prime())
