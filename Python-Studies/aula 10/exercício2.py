#Crie uma função chamada "divide_numbers" que recebe dois
#parâmetros numéricos (A e B) e retorna a divisão de A por B
#utilize try/except para tratar a divisão por zero.


def divide_numbers(A, B):
    try:
        return A / B
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        return None

def main():
    x = int(input("Qual número será dividido: "))
    y = int(input("Qual número será o divisor: "))

    resultado = divide_numbers(x, y)
    if resultado is not None:
        print(f"Resultado da divisão: {resultado}")

main()