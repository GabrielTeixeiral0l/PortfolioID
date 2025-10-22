import random

num = random.randint(1, 10)

while True:
    n = int(input("Adivinhe o número: "))
    if n == num:
        print("Parabéns, acertou!")
        break