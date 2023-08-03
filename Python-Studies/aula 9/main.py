"""
def test(x):
    return (f"O dobro de {x} é {x*2}")

x = test(5)
print(x)"""

"""
def test(msg):
    print(msg)

def dumb():
    return test

v = dumb()
print(type(v))
v("oi")
"""

"""
def teste():
    return "Rodrigo", "Paiva"

nome, sobrenome = teste()
print (nome, sobrenome)
"""

"""
def test (*agrs):
    for i in agrs:
         print(i, end=" ")

test(1, 2, 3, 4, "Rodrigo", 78)
"""

"""
lista = [1, 2, 3, 4, 5]

n1, *n, n2 = lista
print(n1, n, n2)
print (*lista)
# ao usar "*" junto a uma variável pode empacotar e desempacotar dependendo de como é usado
"""

"""
def test(*args):
    print(args)
    args = list(args)
    args[0] = 99
    print (args)
test(1, 2, 3, 4)
"""

def test (*args, **kwargs):
    print(args, kwargs["nome"])

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
test (*lista, *lista2, nome = "Rodrigo")