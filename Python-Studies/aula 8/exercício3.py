#Gerencie um jogador de futebol lendo o nome e quantas partidas ele jogou 
#Depois, leia a quantidade de gols feitas em cada partida
#Coloque tudo num dicionário incluindo o valor total de gols durante o periodo

# Dicionário para armazenar informações dos jogadores e suas partidas
dados_jogadores = {}

def adicionar_gol(jogador, partida, gols):
    if jogador not in dados_jogadores:
        dados_jogadores[jogador] = {"partida": [], "gols": []}
    dados_jogadores[jogador]["partida"].append(partida)
    dados_jogadores[jogador]["gols"].append(gols)

# Exemplo de utilização
adicionar_gol("João", 1, 2)
adicionar_gol("Gabriel", 2, 1)
adicionar_gol("Maria", 1, 3)
adicionar_gol("Jokebede", 2, 0)

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
