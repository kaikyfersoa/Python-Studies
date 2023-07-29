#Crie um programa onde 4 jogadores jogam um dado
#Guarde esses resultados em um dicionário
#No final, coloque esse dicionário em ordem (maior para o menor)

import operator
import random 

dicionario = {}

dicionario['ana'] = random.randint(1,6)
dicionario['jose'] = random.randint(1,6)
dicionario['flavia'] = random.randint(1,6)
dicionario['joao'] = random.randint(1,6)

dicionaro_crescente = dict(sorted(dicionario.items(), key=operator.itemgetter(1), reverse= True))

print(dicionaro_crescente)