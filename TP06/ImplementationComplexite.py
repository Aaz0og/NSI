import matplotlib.pyplot as plt  # Pour faire des graphiques
import random  # Pour faire de l'aléatoire
import time  # Pour manipuler le temps
import sys
# partie I - Recherche d'un minimum
def alea(j):
    '''In : i un entier, la taille de la liste à générer
    Out : une liste de i entiers aléatoires compris entre 0 et 100'''
    liste_aleatoire = []
    for _ in range(j+1):
        n = random.randint(0,100)
        liste_aleatoire.append(n)
    print("Liste aléatoire:",liste_aleatoire)
    return liste_aleatoire

# def Minimum(L):
""" In : L est une liste de nombres non vide
    Out : Le minimum de L"""

# Fonctions nécessaires au test de la complexité des algorithmes, utilisées dans toutes les parties


def TempsAlgo(i, fonction):
    '''In : i un entier, la taille du tableau
    Out : le temps mis par l'algorithme'''
    A = alea(i)  # On fait un tableau rempli de i valeurs aléatoires
    debut = time.time_ns()  # donne l'heure en nanoseconde.
    fonction(A)
    return time.time_ns()-debut


def trace(fonction, imax):
    """ In : fonction est le nom d'une fonction qui agit sur une liste et 
    dont on veut afficher la durée de calcul en fonction de la longueur de la liste
    Out : Affichage du temps en fonction de la longueur de la liste
    Des listes de longueur 0 à imax sont testées
    Il est possible d'enregistrer le graphique"""
    temps = []
    taille = [i for i in range(1, imax+1)]
    for t in taille:
        temps += [TempsAlgo(t, fonction)]
    plt.title("temps de calcul en fonction de la longueur de la liste")
    # On trace la figure les tailles en abscisse,les temps en ordonnées
    plt.plot(taille, temps)
    plt.xlabel('Taille liste')
    plt.ylabel('Temps(ns)')
    plt.show()  # Affichage
    # fig.savefig('graph.png') # si on veut sauvegarder la figure (ATTENTION de changer le nom du fichier pour ne pas écraser les précédents)

# II - algos de tri
# A - Tri par sélection
def TriSelection(A):
    """In : liste de nombres A
    Out : liste triée par sélection"""
    for i in range(len(A)):
        # Trouve le minimum
        idx_min = i
        for o in range(i+1, len(A)):
            if A[idx_min] > A[o]:
                idx_min = o
        # Change le minimum trouvé avec le premier nombre
        A[i], A[idx_min] = A[idx_min], A[i]
    return A

A= alea(10)
print("Après Tri:", TriSelection(A))

def test(a):
    
    return A

"""   
# B - Tri par insertion
#def TriInsertion(A):
    ''' In : liste de nombres A
    Out : liste triée par insertion'''    
#def Inserer(i,A):
    ''' In : liste de nombres A, 
    i indice de la valeur à insérer dans la partie de A qui la précède
    Out : A est triée jusqu'à l'indice i inclus.'''
"""





