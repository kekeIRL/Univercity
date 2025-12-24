import random

n = random.randint(0, 100)
print("guess a number between 0 and 100")
i = 0
while True:
    g = int(input())
    i += 1
    if g == n :
        print("you win!")
        print(f"tries:{i}")
        break
    if g < n:
        print("too low!")
    if g > n:
        print("too high!")
