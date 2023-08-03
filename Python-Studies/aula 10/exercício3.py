#Escreva um programa que solicite ao usuário que digite seu
# nome e a sua idade. Em seguida, tente converter a idade em
# um número inteiro. Se a conversão falhar, informe ao usuario
# que a idade digitada é invalida e continue o programa
# Caso contrário, exiba uma mensagem com o nome e a idade



while True:
    try:
        nome = input("Qual o seu nome? ")
        idade = int(input("Qual a sua idade? "))
        print(f"Olá {nome}, você tem {idade} anos")
        break
    except ValueError:
        print("Você digitou algo errado, tente novamente")