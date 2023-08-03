# Escreva uma funcção que receba uma lista de palavras  como
# entrada e retorne uma lista apenas com palavras que tem mais de 5 letras

def palavras_mais_de_5_letras(lista_palavras):
    return [palavra for palavra in lista_palavras if len(palavra) > 5]

# Exemplo de uso:
lista_palavras = ["python", "linguagem", "programar", "gato", "elefante", "casa"]
palavras_com_mais_de_5_letras = palavras_mais_de_5_letras(lista_palavras)
print(palavras_com_mais_de_5_letras)
