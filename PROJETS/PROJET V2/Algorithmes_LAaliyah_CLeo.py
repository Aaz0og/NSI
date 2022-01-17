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




"""Complexité de l'algo1:
On prend n la longueur de la liste
O(n^4)"""

"""L'algorithme de l'algo 1:
parcours la liste des valeurs des droites verticales et horizontales, et compare toutes les valeurs entre elles,
et si la grandeur de l'espace entre les 2 valeurs verticales est égale aux deux valeurs horizontales comparées, alors 
on ajoute 1 au compteur
le compteur représente le nombre de carrés"""


def algo2(x,y):
    liste_x = []
    liste_y = []
    cpt = 0
    '''Crée une liste qui contient toutes les valeurs possibles pour des longueurs.'''
    for i in range(len(x)):
        for j in range(len(x)):
            if x[j] - x[i] > 0:
                liste_x.append(x[j] - x[i])

    '''Crée une liste qui contient toutes les valeurs possibles pour des largeurs.'''
    for i in range(len(y)):
        for j in range(len(y)):
            if y[j] - y[i] > 0:
                liste_y.append(y[j] - y[i])

    '''Compare les deux listes pour savoir combien il y a de valeurs identiques.'''
    for i in range(len(liste_x)):
        for j in range(len(liste_y)):
            if liste_x[i] == liste_y[j]:
                cpt += 1
    return cpt

x = [ 0,  3, 6, 9]
y = [ 0,  3, 6, 9]
print(algo2(x,y))
for i in range(9):
    pass
    """Complexité de l'algo2:
On prend n la longueur de la liste
O(n*log(n))
"""

"""L'algorithme de l'algo 2:
creer la liste x
creer la liste y
initialiser le compteur à 0
parcourir la liste des longueurs en comparant toutes les longueurs possibles 
les enregistrer dans la liste x si elles sont supérieures à 0
parcourir la liste des largeurs en comparant toute les largeurs possibles 
les enregistrer dans la liste y si elles sont supérieures à 0
parcours la liste x et la liste y et compare chaques valeurs
si elles sont identiques ajouter 1 au compteur (le compteur représente le nombre de carrés)"""
