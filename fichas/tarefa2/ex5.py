import random 


resp = input("Lançar dado? (s/n): ")
while (resp.lower() == "s"):
    num = random.randint(1, 6)
    print(num)
    resp = input("Lançar dado? (s/n): ")

    
