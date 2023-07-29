#Faça um programa que verifique se um número é impar ou par

numero = int(input("Digite um número: "))

if numero%2 == 0:
    print("O número é par")
elif numero%2 == 1:
    print("O número é impar")