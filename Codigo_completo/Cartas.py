import random

valores = ("A", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K")

naipes = ( "♠", "♥", "♦", "♣")

baralho = []

for naipe in naipes:
    for valor in valores:
        baralho.append((valor, naipe))

carta_sorteada = random.choice(baralho)

print(f"Carta sorteada: {carta_sorteada[0]}{carta_sorteada[1]}")

