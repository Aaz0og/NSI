# Détermine l'indice du maximum d'une liste non vide

def indice_maximum_liste(t):
    """
    Renvoie l'int max d'une liste

    Args:
        t (list): Liste d'int

    Returns:
        int: Max
    """
    assert len(t) > 0, "Le tableau est vide"
    m = 0
    for i in range(len(t)):
        if t[i] > t[m]:
            m = i
    return m


"""
La provenance de cette erreur vient du fait que la liste est vide et donc le code ne peut
pas accéder aux valeurs présentes dedans pour éviter cela on peut simplement faire une
vérification de taille au début
help(indice_maximum_liste) --> sers a afficher le texte commenté présent dans une fonction
précondition l1, postcondition l4
Les commentaires réflètent la vérité mais restent très vagues par rapport a l'utilisation de la fonction
"""


def division_euclidienne(a, b):
    """
    Faut la division euclidiene de 2 int, le premier int doit être supérieur ou égal a 0

    Args:
        a (int): Premier int
        b (int): Deuxième int

    Returns:
        q,r: Division euclidienne
    """
    q = 0
    r = a
    while r >= b:
        q += 1
        r -= b
    return q, r


def puissance(x, n):
    """
    Fait la puissance de x par n

    Args:
        x (int): Nombre
        n (int): Puissance

    Returns:
        int: Nombre par puissance x**n
    """
    return x**n

# Le message affiché par python est "Le tableau est vide" il est donc beaucoup plus facile
# de savoir pourquoi une erreur s'est produite


def indice_maximum_liste2(t):
    if len(t) == 0:
        return None
    m = 0
    for i in range(len(t)):
        if t[i] > t[m]:
            m = i
    return m


def tests():
    assert indice_maximum_liste2([2, 3, 1]) == 1, "Erreur max milieu"
    assert indice_maximum_liste2([]) == None, "Erreur liste vide"
    assert indice_maximum_liste2([6, 4, 3, 2]) == 0, "Erreur max au début"
    assert indice_maximum_liste2([1, 2, 3, 6]) == 3, "Erreur max a la fin"
    assert indice_maximum_liste2([-4, -2, -6]) == 1, "Erreur nombres négatifs"
    return str("Aucune erreur, tests indice_maximum_liste2")


print(tests())


def somme_valeurs_liste(t):
    """
    Fonction qui fait comme son nom l'indique la somme des valeurs d'une liste

    Args:
        t (list): Liste d'int

    Returns:
        int: Somme des valeurs de la liste donnée
    """
    s = 0
    for i in range(len(t)):
        s += t[i]
    return s


def tests_somme():
    assert somme_valeurs_liste([1, 2, 3]) == 6, "Erreur addition"
    assert somme_valeurs_liste([-2, -3]) == -5, "Erreur nombres négatifs"
    assert somme_valeurs_liste([1, -2]) == -1, "Erreur négatifs + positifs"
    return str("Aucune erreur, somme_valeurs_liste")


print(tests_somme())

def appartient (v,t):
    i=0
    while i<len(t)-1 and t[i]!=v:
        i=i+1
    return i<len(t)

def tests_appartient():
    assert appartient(4,[1,3,4])==True,"Erreur nombre positif"
    assert appartient(-2,[1,3,4,5,-2])==True,"Erreur nombre négatif"
    assert appartient(6,[6,4,3])==True,"Erreur valeur première"
    assert appartient(6,[1,3,4,6])==True,"Erreur valeur dernière"
    return str("Aucune erreur, appartient")

print(tests_appartient())

def valeur1(chaine):
    s=0
    for c in chaine:
        if c>= "A" and c<= "Z":
            s=s+ord(c)-ord("A")+1
    return s

def valeur2(chaine):
    s=0
    for c in chaine.upper():
        if c>= "A" and c< "Z":
            s=s+ord(c)-ord("A")+1
    return s

def valeur1test():
    assert valeur1("AZ-")==2 
    assert valeur1("AAAZ")==4
#valeur1test()

def valeur2test():
    assert valeur2("AZ-")==2 
    assert valeur2("AAAZ")==4
#valeur2test()


import string
def valeur3(chaine):
    chaine = chaine.upper()
    s=0
    for c in string.ascii_uppercase:
        if c in chaine:
            if c=="Z":
                s+=26
            elif c=="A":
                s+=1
            elif c in string.ascii_uppercase and not c=="A" and not c=="Z": 
                s+=string.ascii_uppercase.index(c)
    return s


def valeur3test():
    assert valeur3("AZ")==27
    assert valeur3("Aza")==27
    return "Aucune erreur, valeur3"
print(valeur3test())

print(valeur3("Arithmancie"))