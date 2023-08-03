#Crie uma função chamada "read_file" que recebe o nome de 
#um arquivo e tenta abri-lo para leitura.
#Se o arquivo não existir, capture a exceção
#FileNotFoundError  e imprima uma mensagem amigável para o usuário.

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("Conteúdo do arquivo:")
            print(content)
    except FileNotFoundError:
        print(f"O arquivo '{file_name}' não foi encontrado. Certifique-se de que o nome do arquivo está correto.")

# Exemplo de uso:
file_name = "arquivo_inexistente.txt"
read_file(file_name)
