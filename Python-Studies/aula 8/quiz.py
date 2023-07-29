#Crie um jogo de perguntas e respostas no python, use dicionários

import random

def criar_perguntas_respostas():
    perguntas_respostas = {
        "Qual o apelido do abelha?": "Rodrigo",
        "Quem é o tio?": "Antonio",
        "Qual é o maior planeta do Sistema Solar?": "Júpiter",
        "Qual a fórmula da água?": "h2o",
        "Em qual avenida fica a FIURJ?": "Rio Branco",
        "Qual é o maior mamífero do mundo?": "Baleia Azul"
    }
    return perguntas_respostas

def jogar():
    perguntas_respostas = criar_perguntas_respostas()
    perguntas = list(perguntas_respostas.keys())
    random.shuffle(perguntas)
    
    pontos = 0
    
    for pergunta in perguntas:
        print(pergunta)
        resposta = input("Sua resposta: ").strip().lower()
        resposta_correta = perguntas_respostas[pergunta].lower()
        
        if resposta == resposta_correta:
            pontos += 1
            print("Resposta correta!")
        else:
            print(f"Resposta incorreta! A resposta correta é: {resposta_correta}")
            pontos -= 1
    
    print(f"Você acertou {pontos} pergunta(s) de um total de {len(perguntas)} perguntas.")
jogar()
