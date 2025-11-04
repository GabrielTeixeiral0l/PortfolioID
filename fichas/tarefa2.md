# Tarefa 2 - Exercícios de Python &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

## Exercício 1

```python
n1 = int(input('Introduz um número: '))
n2 = int(input('Introduz outro número: '))

print("Resultados: ")
print("  Soma = ", n1 + n2)
print("  Subtração = ", n1 - n2)
print("  Multiplicação = ", n1 * n2)
print("  Divisão = ", n1 / n2)
```

## Exercício 2

```python
n = int(input("Introduza um número: "))

r = range(1,11)
for i in r:
    print(f"{n} x {i} = {n*i}")
```

## Exercício 3

```python
n = int(input("Introduza um número: "))

s = int(input("Introduza o inicial: "))

e = int(input("Introduza o final: "))

r = range(s,e+1)
for i in r:
    print(f"{n} x {i} = {n*i}")
```

## Exercício 4

```python
import random 

num = random.randint(1, 6)
print(num)
```

## Exercício 5

```python
import random 


resp = input("Lançar dado? (s/n): ")
while (resp.lower() == "s"):
    num = random.randint(1, 6)
    print(num)
    resp = input("Lançar dado? (s/n): ")
```

## Exercício 6

```python
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
```

## Exercício 7

```python
import random

print(random.randint(1, 1))

print(random.randrange(1,2))

# randint - retorna um número inteiro aleatório entre os valores especificados
# randrange - excluí o ultimo valor
# ou seja randint(1,6) = randrange(1,7)
```

## Exercício 8

```python
import random

num = random.randint(1, 10)

while True:
    n = int(input("Adivinhe o número: "))
    if n == num:
        print("Parabéns, acertou!")
        break
```

## Exercício 9

```python
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
```

## Exercício 10

```python
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
```

## Exercício 11

```python
def bom_dia():
    print("Bom dia!")


bom_dia()
```

## Exercício 12

```python
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
```

## Exercício 13

```python
def boas_vindas(hora):
    if hora <= 12:
        print("Bom dia!")
    elif hora < 20:
        print("Boa tarde!")
    else:
        print("Boa noite!")

hora = int(input("Que horas é agora? "))
boas_vindas(hora)
```

## Exercício 14

```python
# 1 
# 5
# 1

def exemplo():
    n = 5
    print(n)
n = 1
print(n)
exemplo()
print(n)
```

## Exercício 15

```python
# 1
# 5
# 5
def exemplo():
    global n
    n = 5
    print(n)
n = 1
print(n)
exemplo()
print(n)

# global chama uma variavel global
```

## Exercício 16

```python
def tabuada(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")


n = int(input("Introduza um número: "))
tabuada(n)
```
