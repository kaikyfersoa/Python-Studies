#Crie um programa que receba 5 valores int e no final mostre
#A soma apenas dos pares


numeros = [1, 2, 3, 4, 5]

soma = 0

for numero in range(len(numeros)):
    if numero % 2 == 0:
        soma += numero

print(f"A soma dos numeros é: {soma}")