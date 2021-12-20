import random
from collections import deque

def generer_paquet():
    paquet = deque()
    for _ in range(4):
        for i in range(1, 14):
            deque.append(paquet, i)
    random.shuffle(paquet)
    random.shuffle(paquet)
    return paquet


def tour_bataille(paq1, paq2):
    if paq1(0) > paq2(0):
        deque.append(paq1, deque.popleft(paq1))
        deque.append(paq1, deque.popleft(paq2))
        deque.popleft(paq1)
        deque.popleft(paq2)
    elif paq2(0) > paq1(0):
        deque.append(paq2, deque.popleft(paq2))
        deque.append(paq2, deque.popleft(paq1))
        """deque.popleft(paq2)
        deque.popleft(paq1)"""
    elif paq1(0) == paq2(0):
        deque.popleft(paq1)
        deque.popleft(paq2)
    print("Paquet 1", paq1)
    print("Paquet 2", paq2)
    print("----------")


p1 = generer_paquet()
p2 = generer_paquet()
print(p1, "Paq1", p2, "Paq2")
print("----------")


def jeu_bataille(tours):
    i = 0
    for i in range(tours):
        if p1 == True and p2 == True:
            print("Egalite apres", i, "tours")
            return
        if p1 == True:
            print(
                "Le joueur 2 a gagne avec le jeu:",
                p2,
                "Le jeu s'est termine en",
                i,
                "tours",
            )
            return
        if p2 == True:
            print(
                "Le joueur 1 a gagne avec le jeu:",
                p1,
                "Le jeu s'est termine en",
                i,
                "tours",
            )
            return
        tour_bataille(p1, p2)
        i += 1
    print("Nombre de tours maximal atteind paquet 1:", p1, "Paquet 2:", p2)
    return


jeu_bataille(100000)