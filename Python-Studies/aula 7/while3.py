#função append joga os valores para dentro da lista
pares = list()
impares = []
while True:
    n = int(input("Digite um valor"))
    if n == 0:
        break
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
   

print(pares)
print(impares)
