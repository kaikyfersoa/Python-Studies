"""refazendo desafio dos triangulos: 
Acrescentando um recurso que mostra o tipo 
de triangulo formado.

equilátero: todos os lados iguais
isóceles: dois lados iguais, um diferente
escaleno: todos os lados diferentes"""

lado1 = float(input("Qual o tamanho do primeiro lado? "))
lado2 = float(input("Qual o tamanho do segundo lado? "))
lado3 = float(input("Qual o tamanho do terceiro lado? "))

canbe = True

if lado1 < lado2 + lado3 and lado2 < lado3+lado1 and lado3 < lado1+lado2:
    canbe == True
else:
    canbe == False

if canbe == True:
    if lado1 == lado2 == lado3:
        print("Esse triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Esse triângulo é isósceles.")
    else:
        print("Esse triângulo é escaleno.")