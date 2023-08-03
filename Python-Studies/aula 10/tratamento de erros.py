"""
try:
    # Código que pode gerar um erro
    # ...
except TipoDoErro as nomeDoErro:
    # Código a ser executado quando ocorre o erro do tipo especificado
    # ...
else:
    # Código a ser executado se não ocorrer nenhum erro no bloco try
    # ...
finally:
    # Código a ser executado sempre, independentemente de ocorrer um erro ou não
    # ...
"""

# O código só roda quando tudo dentro do try está de acordo com os erros

#While (um loop)
#try (Tenta fazer algo)
#except (Identifica erros (que podem ser identificados por tipo))
#pass (ignora o erro do except)


def main():
    x = getint("What is x: ")
    print(f"X is {x}")

def getint(msg):
    """
    Função para obter um valor inteiro a partir do usuário com tratamento de erros.

    Parâmetros:
        msg (str): A mensagem mostrada ao usuário ao solicitar o valor.

    Retorna:
        int: O valor inteiro válido fornecido pelo usuário.
    """
    while True:
        try:
            # Tentativa de converter a entrada do usuário em um valor inteiro.
            return int(input(msg))
        except ValueError:
            # Se ocorrer um ValueError (entrada inválida), mostra uma mensagem de erro e permite que o usuário tente novamente.
            print(f"Entrada inválida. Por favor, insira um valor inteiro válido.")


def main():
    """
    Função principal para obter um valor inteiro do usuário e exibir o resultado.
    """
    x = getint("Qual é o valor de x: ")  # Pede ao usuário para fornecer um valor inteiro com a mensagem "Qual é o valor de x: ".
    print(f"X é {x}")  # Exibe o resultado com o valor de x fornecido pelo usuário.


main()  # Chama a função principal para iniciar a execução do programa.

