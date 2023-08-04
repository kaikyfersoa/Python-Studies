#Classe "Retângulo"
#Crie uma classe chamada "Cachorro" que possua o método
#__init__ para inicializar as propriedades "nome" e "idade"
#do cachorro. Em seguida, crie um objeto da classe "Cachorro"
#e imprima o nome e a idade do cachorro

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

# Solicitando as informações do retângulo ao usuário
largura_retangulo = float(input("Digite a largura do retângulo: "))
altura_retangulo = float(input("Digite a altura do retângulo: "))

# Criando um objeto da classe Retangulo com as informações fornecidas pelo usuário
meu_retangulo = Retangulo(largura_retangulo, altura_retangulo)

# Calculando e imprimindo a área do retângulo
area = meu_retangulo.calcular_area()
print(f"Área do retângulo: {area}")