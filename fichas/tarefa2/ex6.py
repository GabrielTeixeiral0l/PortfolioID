import random 


resp = input("Quantos dados (1, 2, s - sair) ")
while (resp.lower() != "s"):
    num = random.randint(1, 6)
    if (resp == "2"):
        num2 = random.randint(1, 6)
        print(num, num2)
    else:
        print(num)
    resp = input("Quantos dados (1, 2, s - sair) ")

    
