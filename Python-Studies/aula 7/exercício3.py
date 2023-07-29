#Mostre o fatorial de um novo numero enviado pelo usuário
#Ex: 5x4x3x2x1 = 120

def fatorial():
    numero = int(input("Digite um número: "))
    resultado = 1

    while numero != 0:
        resultado *= numero
        numero -= 1

    print(f"O resultado da fatoração foi: {resultado}")

fatorial()