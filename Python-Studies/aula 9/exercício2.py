#Crie uma função que receba uma lista de numeros como entrada
# e retorne o maior número presente na lista

def num_list (*args):
    args = (args)
    sorted(args, reversed=False)
    print(args) 
    return

lista = [1, 4, 14, 5, 19, 22]

num_list(*lista)