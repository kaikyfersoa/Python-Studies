# Usando while

p = int(input("Qual sua idade? "))

while p != 0 and p < 99:
    print(f"Você tem {p} anos")
    p = int(input("Qual sua idade?"))
print("FIM")

