from mesures import *
from donnees import jeux


def algo1(x,y):
    cpt = 0
    for i in range(len(x) - 1):
        for j in range(len(x) - 1):
            for k in range(len(y) - 1):
                for l in range(len(y) - 2):
                    if x[i] - x[j] == y[k] - y[l]:
                        cpt += 1
    return cpt

"""
Complexité de l'algo1:
On prend n la longueur de la liste
O(n^4)
L'algorithme de l'algo 1:
parcours la liste des valeurs des droites verticales et horizontales, et compare toutes les valeurs entre elles,
et si la grandeur de l'espace entre les 2 valeurs verticales est égale aux deux valeurs horizontales comparées, alors 
on ajoute 1 au compteur
le compteur représente le nombre de carrés
"""


def algo2(x,y):
    """
    Trouve le nombre de carres dans deux listes pour chaque absisse

    Args:
        x (list): liste des cordonnees en x
        y (lsit): liste des coordonnees en y

    Returns:
        int: Nombre de carres
    """
    liste_x = []
    liste_y = []
    resul = 0
    '''Crée une liste qui contient toutes les valeurs possibles pour des longueurs.'''
    for i in range(len(x)):
        for j in range(len(x)):
            if x[j] - x[i] > 0:
                liste_x.append(x[j] - x[i])
                print("liste_x:",liste_x)

    '''Crée une liste qui contient toutes les valeurs possibles pour des largeurs.'''
    for i in range(len(y)):
        for j in range(len(y)):
            if y[j] - y[i] > 0:
                liste_y.append(y[j] - y[i])
                print("liste_y:", liste_y)

    '''Ici on compare les 2 listes et si les valeurs sont identiques on ajoute 1 au compteur résul'''
    for i in range(len(liste_x)):
        for j in range(len(liste_y)):
            if liste_x[i] == liste_y[j]:
                resul += 1
                
    return resul

x = [ 0, 2, 5, 10]
y = [ 0, 3, 5]
print(algo2(x,y))

"""
Complexité de l'algo2:
On prend n la longueur de la liste
O(n*log(n))
L'algorithme de l'algo 2:
creer la liste x
creer la liste y
initialiser le compteur à 0
parcourir la liste des longueurs en comparant toutes les longueurs possibles 
les enregistrer dans la liste x si elles sont supérieures à 0
parcourir la liste des largeurs en comparant toute les largeurs possibles 
les enregistrer dans la liste y si elles sont supérieures à 0
parcours la liste x et la liste y et compare chaques valeurs
si elles sont identiques ajouter 1 au compteur (le compteur représente le nombre de carrés)
"""
