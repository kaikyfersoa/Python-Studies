#Se o salário for maior que 1250, aumento de 15. 
#se o salario for menor que ou igual 1250, aumento de 10.

salario = float(input("Digite o seu salário"))

if salario > 1250:
    print(f"Seu novo salário é: {salario + (salario*15/100)}")
elif salario <= 1250:
    print(f"Seu novo salário é: {salario + (salario*10/100)}")