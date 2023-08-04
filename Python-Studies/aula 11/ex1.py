#Classe "Cachorro":
#Crie uma classe chamada "Cachorro" que possua o método
#__init__ para inicializar as propriedades "nome" e "idade"
#do cachorro. Em seguida, crie um objeto da classe "Cachorro"
#e imprima o nome e a idade do cachorro. 

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Solicitando as informações do cachorro ao usuário
nome_cachorro = input("Digite o nome do cachorro: ")
idade_cachorro = int(input("Digite a idade do cachorro: "))

# Criando um objeto da classe Cachorro com as informações fornecidas pelo usuário
meu_cachorro = Cachorro(nome_cachorro, idade_cachorro)

# Imprimindo o nome e a idade do cachorro
print(f"Nome do cachorro: {meu_cachorro.nome} Idade do cachorro: {meu_cachorro.idade}")