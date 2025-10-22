import random

print("Configurações: ")

qtent = int(input("Quantividade de tentativas: "))

print("Intervalo: ")
i1 = int(input("Intervalo inicial: "))

i2 = int(input("Intervalo final: "))

num = random.randint(i1, i2)

tent = 1

while tent <= qtent:
    n = int(input("Adivinhe o número: "))
    if n == num:
        print("Parabéns, acertou!")
        break
    elif (tent == qtent):
        print("Perdeu!")
        break
    tent += 1
    
