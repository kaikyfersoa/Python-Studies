#Crie um dicionário que guarde o nome, ano de nascimente a idade
#o ano de contratação e o salário de um funcionário.
#Calcule e acrescente no dicionário quantos anos a pessoa se aposentará

dic = {"nome": "Rodrigo", 
       "nascimento": 2000,
       "idade": 23,
       "contratação": 2022,
       "Salário": 50000
       }

resultado = dic["contratação"] + 35

print (f"Você poderá se aposentar no ano de {resultado}")