#Três retas formam um triângulo?

a = float(input("Digite o valor da reta a"))
b = float(input("Digite o valor da reta b"))
c = float(input("Digite o valor da reta c"))

if a < b+c and b < c+a and c < a+b:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")