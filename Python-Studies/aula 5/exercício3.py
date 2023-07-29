""" Escreva um programa que leia dois numeros inteiros e compare-os
mostrando na tela uma mensagem:
- O primeiro número é maior
- O segundo número é maior
- Não existe valor maior, os dois são iguais"""

num1 = float(input("Qual o primeiro número? "))
num2 = float(input("Qual o segundo número? "))

if num1 > num2:
    print("O primeiro número é maior")
elif num2 > num1:
        print("O segundo numero é maior")
elif num1 == num2:
      print("Os dois números são iguais")
