phrase = input("Enter a phrase: ").lower()
count = 0

for letter in phrase:
    match(letter):
        case "a" :
            count += 1
        case "e":
            count += 1
        case "i":
            count += 1
        case "o":
            count += 1
        case "u":
            count += 1

for i in range (len(phrase)):

    match(phrase[i]):
        case "a" :
            count += 1
        case "e":
            count += 1
        case "i":
            count += 1
        case "o":
            count += 1
        case "u":
            count += 1

print(count)

print(phrase[0] + phrase[1] + phrase[2])

for i in range (3):
    print(phrase[len(phrase) - i-1])

print(phrase[len(phrase)-3] + phrase[len(phrase)-2] + phrase[len(phrase)-1])