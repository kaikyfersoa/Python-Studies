""" Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar no serviço militar,
se é a hora exata de se aistar ou se já passou do tempo do alistamento.
O seu programa também deverá mostrar o tempo que falta ou o que passou do prazo"""

nascimento = int(input("Em qual ano você nasceu? "))
atual = int(input("Em que ano estamos? "))

if atual - nascimento <= 17:
    print ("Você precisa se alistar ano que vem")
elif atual - nascimento == 18:
        print ("Está na hora de você se alistar!")
elif atual - nascimento > 18:
   print(f"Você está {(atual-nascimento)-18} anos atrasado. ")
