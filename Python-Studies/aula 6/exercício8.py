#Leia o peso de 5 pessoas e mostre o maior e o menor peso digitado

peso1 = float(input("Digite seu peso: "))
peso2 = float(input("Digite seu peso: "))
peso3 = float(input("Digite seu peso: "))
peso4 = float(input("Digite seu peso: "))
peso5 = float(input("Digite seu peso: "))

lista = [peso1, peso2, peso3, peso4, peso5]

for peso in range(len(lista)):
    print(sorted(lista))
    break