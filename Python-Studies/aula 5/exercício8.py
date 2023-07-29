"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule o IMC e mostre seu status de acordo com a tabela abaixo:

entre 18,5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida"""

peso = float(input("Quanto você pesa em quilos? "))
altura = float(input("Qual sua altura em metros? "))

imc = peso/altura**2

if imc == 18 and imc <= 25:
    print("Você está no peso ideal")
elif imc > 25 and imc <= 30:
    print("Você está sobrepeso")
elif imc > 30 and imc <= 40:
    print("Você é obeso")
elif imc > 40:
    print("Você é obeso mórbido")