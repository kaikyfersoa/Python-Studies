#Utilizando str para corrigir possíveis "erros" do usuário. 

#upper deixa o texto em maiúsculo e lower em minúsculo, strip tira o espaço

sexo = str.upper(input("Qual seu sexo? [M/F]")).strip()

while sexo not in "MF":
    print("Digite um valor valido [M/F]")
    sexo = str(input("Qual seu sexo? [M/F]"))

print(f"O seu sexo é {sexo}")