#Agora faça o exercício acima aceitar vários jogadores,
#inclua um sistema para visualizar detalhes do 
#aproveitamento de cada jogador

dados_jogadores = {}
jogador_usuario = ""
partida_usuario = int
gols_usuario = int

def adicionar_gol(jogador, partida, gols):
    if jogador not in dados_jogadores:
        dados_jogadores[jogador] = {"partida": [], "gols": []}
    dados_jogadores[jogador]["partida"].append(partida)
    dados_jogadores[jogador]["gols"].append(gols)

# Exemplo de utilização
adicionar_gol(jogador_usuario, partida_usuario, gols_usuario)

# preciso fazer uma lista vazia, colocar um while pra adicionar jogadores até o usuario dizer que quer parar



# Função para calcular o total de gols de um jogador
def total_gols(jogador):
    return sum(dados_jogadores[jogador]["gols"])

# Imprimir os dados dos jogadores e seus totais de gols 
for jogador, dados in dados_jogadores.items():
    print(f"Jogador: {jogador}")
    for i in range(len(dados["partida"])):
        print(f"Partida {dados['partida'][i]} - Gols: {dados['gols'][i]}")
    print(f"Total de gols: {total_gols(jogador)}")
    print( ) #para espaço
