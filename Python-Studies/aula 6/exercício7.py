#monte um código para dizer se um numero informado é primo

numero = int(input("Digite um numero primo: "))
start = 2
end = numero
step = 1

for i in range(start, end, step):
    if numero % i == 0:
       print("Esse número não é primo")
       break
    elif numero % i == 1:
        print("Esse número é primo")
        break
        