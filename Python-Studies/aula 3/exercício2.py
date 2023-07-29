# Leia o comprimento do cateto oposto e do cateto adjascente 
#de um triangulo retangulo. calcule e mostre o comprimento da hipotenusa

from math import hypot

CO = float(input("Qual o valor do cateto oposto? "))
CA = float(input("Qual o valor do cateto adjascente? "))

print(hypot(CA, CO))