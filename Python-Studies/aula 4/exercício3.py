#programa que leia quilometragem de um carro
#acima de 80 ele é multado

quilometragem = float(input("Quantos quilometros por hora você estava? "))

if quilometragem < 80:
    print("Você está livre")
elif quilometragem > 80:
    print("Você foi multado, colega")