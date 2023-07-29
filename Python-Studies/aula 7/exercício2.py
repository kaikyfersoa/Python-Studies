#Desenvolva uma mini calculadora em que seja permitido:
#Somar, multiplicar, mostrar maior, adicionar novos números e sair

def calculadora():

    while True:
        
        numero_1 = int(input("Digite o primeiro número"))
        numero_2 = int(input("Digite o segundo número"))
        
        print("opções: 1(somar), 2(multiplicar), 3(mostrar maior), 4(trocar numeros), 5(sair)")
        opção = input(str("Digite sua opção "))

        if opção == "1":
            print(f"A soma dos dois numeros é {numero_1 + numero_2}")
        elif opção == "2":
            print(f" {numero_1} vezes {numero_2} é igal a: {numero_1 * numero_2}")
        elif opção == "3":
            if numero_1 > numero_2:
                print(f"O maior número é {numero_1}")
            elif numero_2 > numero_1:
                print(f"O maior número é o {numero_2}")
            else: 
                print("Os números são iguais")
        if opção == "4":
           continue
        if opção == "5":
            break


calculadora()