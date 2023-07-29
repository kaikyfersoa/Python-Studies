#Leia o primeiro termo e a razão de uma PA. Depois, mostre
#Os 20 primeiros termos.

primeiro_termo = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razão? "))


for i in range(primeiro_termo, primeiro_termo*21, razao):
    print(i)