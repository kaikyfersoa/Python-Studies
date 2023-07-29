# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# A prestação mensal não pode exceder 30% do salário ou o empréstimo será negado

casa = float(input("Quanto custa a casa? "))
prestações = int(input("Em quantas parcelas você quer pagar? "))
salario = float(input("Quanto você ganha"))

if (30%salario) > (casa/prestações):
    print("Você pode pegar o empréstimo")
else:
    print("Você não pode pegar o empréstimo")