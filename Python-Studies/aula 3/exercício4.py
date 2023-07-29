#Faça um programa que leia o nome de 4 alunos e escreva na tela 
#o nome do escolhido para apagar o quadro

import random

a1 = input("Nome do primeiro aluno")
a2 = input("Nome do segundo aluno")
a3 = input("Nome do terceiro aluno")
a4 = input("Nome do quarto aluno")

sorteia = (a1, a2, a3, a4)

print("O sorteado foi:", random.choice(sorteia))