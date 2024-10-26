from platform import system

cows = int(input("How many cows? "))
chickens = int(input("How many chickens? "))
bees = int(input("How many bees? "))


legs = (cows * 4) + (chickens * 2) + (bees * 6)

print(legs)

#currency coverter

euro = float(input("How many euros? "))
usd = euro * 1.02

print(usd)

#Holiday

holiday = int(input("""Where do you want to go:
1) Go to Europe
2) Go camping
3) Go on a cruise
"""))

# if holiday == "1":
#     print("Buy an air ticket")
# elif holiday == "2":
#     print("Buy a tent")
# else:
#     print("Buy a swimming costume")

match holiday:
    case 1: print("Buy an air ticket")
    case 2: print("Buy a tent")
    case 3: print("Buy a swimming costume")

print("Have fun")

#Secret message

phrase = input("enter a phrase: ")

if len(phrase) >= 10:

    print(phrase[0])
    print(phrase[4])
    print(phrase[-1])
else:
    print("not enough")

#Maths hw

w = int(input("what is the width "))
l = int(input("what is the length "))

if w == l:
    print("square")
else:
    print("rectangle")
print(w * l)

#Letter replace


sen = input("enter a sentence: ")

def replace_phrase(s):
    srt = ""
    for i in range(len(s)):
        if s[i] == "e":
            srt = srt + "3"
        elif s[i] == "a":
            srt = srt + "@"
        else:
            srt = srt + s[i]
    return srt

print(replace_phrase(sen))