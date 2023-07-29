# Leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente

import math

angulo = float(input("Digite um ângulo qualquer: "))

seno = math.sin(math.radian(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O valor do ângulo é: {angulo}")
print(f"O valor do seno é: {seno}")
print(f"O valor do cosseno é: {cosseno}")
print(f"O valor da tangente é: {tangente}")