#Melhore o jogo de advinhação onde o computador "pensa"
#em um número. Mostre quantos palpites o usuário usou

import random

def jogo_advinhacao():
   
    numero = random.randint(1, 10)
    tentativas = 0
    palpite = list()
    while palpite != numero:
        
            palpite = int(input("Digite o seu palpite: "))
            tentativas = tentativas + 1

            if palpite == numero:
                print(f"Você acertou, o número é {numero}. Demorou apenas {tentativas} tentativas!")
                break



jogo_advinhacao()