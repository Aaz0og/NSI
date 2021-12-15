import file, random


def generer_paquet():
    """
    Generer un paquet aleatoirement

    Returns:
        liste: paquet melange avec 52 cartes
    """
    paquet = file.creer_file()
    for _ in range(4):
        for i in range(1, 14):
            file.ajouter_file(paquet, i)
    random.shuffle(paquet)
    random.shuffle(paquet)
    return paquet


def tour_bataille(paq1, paq2):
    """
    Actions a effectuer apres chaques tours

    Args:
        paq1 (list): Paquet du premier joueur
        paq2 (list): Paquet du deuxieme joueur
    """
    if file.premier_file(paq1) > file.premier_file(paq2):
        file.ajouter_file(paq1, file.premier_file(paq1))
        file.ajouter_file(paq1, file.premier_file(paq2))
        file.retirer_file(paq1)
        file.retirer_file(paq2)
    elif file.premier_file(paq2) > file.premier_file(paq1):
        file.ajouter_file(paq2, file.premier_file(paq2))
        file.ajouter_file(paq2, file.premier_file(paq1))
        file.retirer_file(paq2)
        file.retirer_file(paq1)
    elif file.premier_file(paq1) == file.premier_file(paq2):
        file.retirer_file(paq1)
        file.retirer_file(paq2)
    print("Paquet 1", paq1)
    print("Paquet 2", paq2)
    print("----------")


p1 = generer_paquet()
p2 = generer_paquet()
print(p1, "Paq1", p2, "Paq2")
print("----------")


def jeu_bataille(tours):
    """
    Regles de victoire pour la partie et aussi deroulement qui appelle les fonctions

    Args:
        tours (int): Nombre de tours max a effectuer
    """
    i = 0
    for i in range(tours):
        if file.file_vide(p1) == True and file.file_vide(p2) == True:
            print("Egalite apres", i, "tours")
            return
        if file.file_vide(p1) == True:
            print(
                "Le joueur 2 a gagne avec le jeu:",
                p2,
                "Le jeu s'est termine en",
                i,
                "tours",
            )
            return
        if file.file_vide(p2) == True:
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