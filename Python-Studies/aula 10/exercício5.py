#Crie um programa que solicite ao usuário que digite um valor numerico inteiro.
#Em seguida, tente encontrar o fatorial desse número.
#Utilize try e except para tratar a inserção de valores não inteiros e numericos negativos.

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def main():
    try:
        valor = int(input("Digite um valor numérico inteiro: "))

        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        
        resultado = calcular_fatorial(valor)
        print(f"O fatorial de {valor} é: {resultado}")
    
    except ValueError as e:
        print(f"Erro: {e}")
    except RecursionError:
        print("Erro: O valor é muito grande para calcular o fatorial.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
