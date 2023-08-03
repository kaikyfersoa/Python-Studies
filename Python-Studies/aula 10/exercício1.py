#Escreva um programa que peça ao usuário para digitar 
#Um número inteiro e, em seguida, imprima o dobro do numero
# utilize try/except para lidar com a possibilidade de lidar com
#valores não numericos

def main():
    x = getint("What is x: ")
    x = x*2
    print(f"X x 2 is: {x}")

def getint(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(f"X is invalid")

main()
