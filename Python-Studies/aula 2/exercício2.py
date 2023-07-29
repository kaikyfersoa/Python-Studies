#Calcular área da parede

altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))

area = (largura * altura)

print(f"A área da parede é: {area}"
    f"Para pintar essa parede é necessário {area / 2} litros de tinta")

#ou {(largura * altura)/2}