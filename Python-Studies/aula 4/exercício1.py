#Crie um jogo que faça o computador pensar em um número de 0 até 5 e 
#permita o usuário ter um chute para acertar

import random 

lista = [0, 1 ,2 ,3, 4, 5]

numero = int(input("Digite um número de 0 até 5: "))

sorteado = (random.choice(lista))

print(f"O número sorteado foi: {sorteado}")

if numero == sorteado:
    print("Parabens, você acertou")
elif numero != sorteado:
    print("você errou")