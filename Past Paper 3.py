# #Crate name
from jupyter_server.auth import passwd

petname = input("enter your pet name: ")

surname = input("enter your surname")

myPetsName = petname +" "+ surname

temp = ""
for i in myPetsName:
    if i.upper() == "S":
        i = "$"
    temp += i

myPetsName = temp
print(myPetsName)

for x in myPetsName:
    print(x.upper())

#password
fname = input("enter your first name: ")
lname = input("enter your last name: ")

fullName = fname + " " + lname

temp = ""

for i in fullName:
    if (i.upper() == "A") or (i.upper() == "E") or (i.upper() == "I") or (i.upper() == "O") or (i.upper() == "U"):
        i = "@"

    temp += i


print(temp)

firstTwo = fname[0] + fname[1]

lastTwo = lname[len(lname)-2] + lname[len(lname)-1]

password = firstTwo + lastTwo + "-"
score = 0

for i in fullName:
    if (i.upper() == "A") or (i.upper() == "E") or (i.upper() == "I") or (i.upper() == "O") or (i.upper() == "U"):
        score += 1

password += str(score)
fullName = temp
print(password)