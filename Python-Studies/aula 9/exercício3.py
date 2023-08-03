# Escreva uma funcção que receba uma lista de palavras  como
# entrada e retorne uma lista apenas com palavras que tem mais de 5 letras

dic = {"nomes": 0}
nomes = ["Rodrigo", "Maria", "Mariana", "Juliana", "João"]

def nome5 (x, y):
    dic = {x:y}
    d1 = {x: y for x, y in  dic}
    