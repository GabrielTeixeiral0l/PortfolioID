def boas_vindas(hora):
    if hora <= 12:
        print("Bom dia!")
    elif hora < 20:
        print("Boa tarde!")
    else:
        print("Boa noite!")

hora = int(input("Que horas é agora? "))
boas_vindas(hora)