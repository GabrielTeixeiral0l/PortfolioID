def bom_dia():
    print("Bom dia!")

def boa_tarde():
    print("Boa tarde!")

def boa_noite():
    print("Boa noite!")


hora = int(input("Que horas é agora? "))

if hora <= 12:
    bom_dia()
elif hora < 20:
    boa_tarde()
else:
    boa_noite()