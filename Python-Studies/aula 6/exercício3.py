#Desenvolva um programa que calcule a soma de todos 
#Os números múltiplos de três entre 1 e 500
#E mostre quantos números são divisiveis

soma = 0
divisiveis = 0

for num in range(1, 501):
    if num % 3 == 0:
        soma += num
        divisiveis += 1

print(f"A soma é: {soma}")
print(f"A quantidade de números divisíveis por três é: {divisiveis}")
