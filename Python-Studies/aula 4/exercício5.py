#faça um programa que leia 3 valores e diga o maior e o menor valor

num1 = int(input("Diga o primeiro numero"))
num2 = int(input("Diga o segundo numero"))
num3 = int(input("Diga o terceiro numero"))

if num1 > num2 and num1 > num3:
    print(f"O maior valor é: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior valor é {num2}")
elif num3 > num1 and num3 > num2:
    print(f"O maior valor é: {num3}")

if num1 < num2 and num1 < num3:
    print(f"O menor valor é: {num1}")
elif num2 < num1 and num2 < num3:
    print(f"O menor valor é {num2}")
elif num3 < num1 and num3 < num2:
    print(f"O menor valor é: {num3}")
