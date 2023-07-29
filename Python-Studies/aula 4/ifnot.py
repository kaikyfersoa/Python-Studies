# if not aceita tudo, menos o que a condição "propõe". 
#strip retira os espaços
# if com in inclui qualquer coisa dentro da condição

name = input("What is your name? ").strip()

if not name == "Rodrigo":
    print("Nice to meet you!")
else:
    print("Hi")