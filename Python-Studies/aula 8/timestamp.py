from datetime import datetime

try:
    data_input = input("Digite uma data e hora no formato 'dd/mm/aaaa hh:mm:ss': ")
    formato = "%d/%m/%Y %H:%M:%S"
    data_hora = datetime.strptime(data_input, formato)
    timestamp = int(data_hora.timestamp())
    print(f"O timestamp correspondente à data e hora digitadas é: {timestamp}")
except ValueError:
    print("Formato de data e hora inválido. Certifique-se de seguir o formato correto.")