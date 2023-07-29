"""Elabore um programa que calcule o valor
a ser pago por um produto, considerando
o seu preço normal e a condição de pagamento:
- à vista dinheiro: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cratão: preço formal
- 3x ou mais no cartão: 20% de juros"""

produto = 500

print("Métodos de pagamento:")
print("01: Dinheiro")
print("02: Cartão")

metodo = input("Qual o método de pagamento utilizado? ")

if metodo == "01" or metodo == "1":
    print(f"Você irá pagar {produto - (produto/10)}")
elif metodo == "02" or metodo == "2":
    parcelas = int(input("Em quantas vezes você irá pagar? "))
    if parcelas == 1:
        print(f"Você irá pagar {produto - (produto*0.05)}")
    elif parcelas == 2:
        print(f"Você irá pagar duas parcelas de {produto/2}")
    elif parcelas >= 3:
        print(f"Você irá pagar {parcelas} parcelas de {(produto + (produto/100*20)) / parcelas}")
