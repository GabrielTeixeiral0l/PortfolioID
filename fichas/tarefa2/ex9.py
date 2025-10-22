import random

num = random.randint(1, 10)

tent = 1

while tent <= 3:
    n = int(input("Adivinhe o número: "))
    if n == num:
        print("Parabéns, acertou!")
        break
    elif (tent == 3):
        print("Perdeu!")
        break
    tent += 1
    
