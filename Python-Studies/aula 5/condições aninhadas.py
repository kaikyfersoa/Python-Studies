#condições aninhadas

name = input("What is your name: ")


if name == "rodrigo":
    print("Nice to meet you") 
    age = int(input("What is your age: "))
    if age >= 18:
        print("You are getting older")
    elif age == 16:
        print("You are sixteen")
    else:
        print("You are too young")
else: 
    print("You are not rodrigo")
    if name == "pedro":
        print("Hi Pedro")