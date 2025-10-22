n = int(input("Introduza um número: "))

s = int(input("Introduza o inicial: "))

e = int(input("Introduza o final: "))

r = range(s,e+1)
for i in r:
    print(f"{n} x {i} = {n*i}")

