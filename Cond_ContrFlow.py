import random

rnd = random.randint(1,201)
print(rnd)

if rnd > 100:
    print("greater than 100")
elif rnd < 100:
    print("less than 100")
else:
    print("equals 100")