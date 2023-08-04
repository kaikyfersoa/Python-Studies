#Classe "pessoa":
#Crie uma classe chamada "pessoa" que possus o método __init__
#para inicializar as propriedades "nome", "idade" e "profissão" 
#da pessoa. Em seguida, crie um objeto da classe "pessoa" e imprima
#todas as suas informações (nome, idade e profissão)

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

nome_pessoa = input("Qual o seu nome? ")
idade_pessoa = int(input("Qual a sua idade? "))
profissao_pessoa = input("Qual a sua profissão? ")

pessoa = Pessoa(nome_pessoa, idade_pessoa, profissao_pessoa)

print(f"Olá {pessoa.nome}, você tem {pessoa.idade} e trabalha como {pessoa.profissao}. ")