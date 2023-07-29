"""Crie um programa que leia duas notas de um aluno, calcule sua média,
mostrando uma mensagem no final de acordo com a média atingida:
media abaixo de 5 = reprovado
entre 5 e 6,9 = recuperação
7 ou superior = aprovado
"""

nota1 = float(input("Qual foi a sua primeira nota?"))
nota2 = float(input("Qual foi a sua segunda nota?"))


if (nota1+nota2)/2 <= 4.9:
    print("Reprovado")
elif (nota1+nota2)/2 >=5 and (nota1+nota2)/2 <= 6.9:
        print("Você está de recuperação")
elif (nota1+nota2)/2 >= 7:
            print("Você foi aprovado")