"""A confederação nacional de natação precisa de um programa que leia o 
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

idade = int(input("Qual a sua idade? "))

if idade <= 9:
    print("Categoria: Mirim")
elif idade > 9 and idade <= 14:
    print("Categoria: Infantil")
elif idade > 15 and idade <= 19:
    print("Categoria Júnior")
elif idade > 20 and idade <= 25:
    print("Categoria: Sênior")
elif idade > 25:
    print("Categoria: Master")