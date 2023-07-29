#Faça um programa que diga se um número é par ou impar

n = int(input("Diga um número: "))

print("O número é par" * (n % 2 == 0), "O número é ímpar" * (n % 2 != 0))