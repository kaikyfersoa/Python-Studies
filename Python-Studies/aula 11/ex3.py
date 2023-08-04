#Classe "Aluno"
#Crie uma classe chamada aluno que possua o método __init__
#para inicializar as propriedades "nome" e "nota" do aluno.
#Em seguida, crie dois objetos da classe "Aluno" e verifique
#qual dos dois obteve a maior nota

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

# Solicitando as informações do primeiro aluno ao usuário
nome_aluno1 = input("Digite o nome do primeiro aluno: ")
nota_aluno1 = float(input("Digite a nota do primeiro aluno: "))

# Criando o objeto do primeiro aluno
aluno1 = Aluno(nome_aluno1, nota_aluno1)

# Solicitando as informações do segundo aluno ao usuário
nome_aluno2 = input("Digite o nome do segundo aluno: ")
nota_aluno2 = float(input("Digite a nota do segundo aluno: "))

# Criando o objeto do segundo aluno
aluno2 = Aluno(nome_aluno2, nota_aluno2)

# Verificando qual dos alunos obteve a maior nota
if aluno1.nota > aluno2.nota:
    print(f"O aluno {aluno1.nome} obteve a maior nota.")
elif aluno2.nota > aluno1.nota:
    print(f"O aluno {aluno2.nome} obteve a maior nota.")
else:
    print("Os alunos obtiveram a mesma nota.")
