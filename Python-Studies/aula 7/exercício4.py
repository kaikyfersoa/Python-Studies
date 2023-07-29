#Refaça p desafio da PA mostrando os 20 primeiros termos
#E pergunte ao usuário quantos termos a mais ele quer ver.
#O programa encerra quando ele disser que quer mostrar 0

def PA():
    
    primeiro_termo = int(input("Qual o primeiro termo? "))
    razao = int(input("Qual a razão? "))
    quantidade = 20
     
    while True:
        for i in range(primeiro_termo, primeiro_termo*quantidade, razao):
            print(i, end=' ')
        a_mais = (int(input("Quantos termos a mais você quer ver?")))
        if a_mais != 0:
            quantidade += a_mais
            print(i)
        else:
            break

PA()