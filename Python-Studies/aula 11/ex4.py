#Classe "círculo"
#Crie uma classe chamada "círculo" que possua o método __init__
#para iniciaizar a propriedade "raio" do círculo.
#em seguida, crie um objeto da classe "círculo" e calcule e imprima a área do círculo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio

def get_area(raio):
    area = 3.14 * (raio ** 2)
    return area

raio = float(input("Qual o raio do círculo? "))

circulo1 = Circulo(raio)

print(f"A área do círculo de raio {circulo1.raio} é {get_area(circulo1.raio)}")
