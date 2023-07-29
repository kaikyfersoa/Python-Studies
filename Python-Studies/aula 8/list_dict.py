"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobra = [n for n in lista if n % 2 == 0]
dobra = [n if n % 2 == 0 else None for n in lista]
print (dobra)
"""

"""
nomes = ["Rodrigo", "Pedro", "Antonio"]
lista_modificada = [nome.replace("o", "a") for nome in nomes]
print(lista_modificada)
"""

"""
lista = [
    ("chave", "valor"),
    ("chave2", "valor2")
]
d1 = {k: v for k, v in lista}
print(d1)
"""

"""
locadora = []

filme1 = {"Nome": "Vingadores", "ano": 2013}
filme2 = {"Nome": "Suckerpunch", "ano": 2012}
filme3 = {"Nome": "Barbie", "ano": 2023}

locadora = [filme1, filme2, filme3]

print(locadora[2]["ano"]) #Buscamos pela posição e key quando quisermos um valor específico
"""

"""
filme5 = {"nome": "x", "ano": "2020", "chave": "valor"}

for k, v in filme5.items():
    print(f"A chave é: {k} e o valor é: {v}")
"""

"""
jogadores = []
jogador = {}

while True:
    jogador["nome"] = input("Qual o nome do jogador? ")
    jogador["partidas"] =int(input("Quantas partidas jogou:"))
    jogadores.append(jogador)
    resp = input("Quer continuar? [S/N]").upper()[0]
    if resp == "N":
        break
"""

"""
d1 = {"nomes":["Rodrigo", "Pedro"]}
print(d1["nomes"][1])
"""

"""
d2 = {"nomes": [{"nome": "Rodrigo", "nome2": "Pedro"}]}

print (d2["nomes"][0]["nome2"])
"""


#difionário funciona com dois objetos: chaves e valor