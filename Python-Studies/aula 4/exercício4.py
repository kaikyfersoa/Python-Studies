#faça um programa que leia distância de uma viagem
#distancia menor ou igual a 200km, 50centavos por km
#acima disso, cobre 45 centavos

distancia = float(input("Quantos quilometros você rodou? "))

if distancia <= 200:
    print(f"Você vai pagar {distancia*0.5}")
elif distancia > 200:
    print(f"Você vai pagar {distancia*0.45}")