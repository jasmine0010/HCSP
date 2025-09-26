import random

def flip():
    n = random.randint(0, 1)
    return "Heads" if n == 1 else "Tails"

for i in range(10):
    print(flip())