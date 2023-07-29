# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# Qual será a base de conversão:
# 1 para binário, 2 para octal, 3 para hexadecimal

numero = int(input("Qual numero você quer converter: "))
 
conversao = (input("Qual tipo de conversão você quer fazer? "))

if conversao == "bin":
    print(f"{bin(numero)}")
elif conversao == "octal":
      print(f"{oct(numero)}")
elif conversao == "hexa":
      print(f"{hex(numero)}")