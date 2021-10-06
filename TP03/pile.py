class Cellule:
    def __str__(self):
        aff = str(self.valeur)
        return aff

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant


"""
c3 = Cellule(5, None)
c2 = Cellule(7, c3)
c1 = Cellule(19, c2)
print(c1.valeur)
print(c1.suivant.valeur)
print(c1.suivant.suivant.valeur)
print(c1.suivant.suivant.suivant)
c1.suivant.valeur
"""


class Pile:
    def __init__(self, sommet=0, taille=0):
        self.sommet = Cellule(sommet, None)
        self.taille = taille

    def estVide(self):
        if self.taille == 0:
            return True
        else:
            return False

    def valeurSommet(self):
        return self.sommet.valeur

    def empiler(self, ajout):
        self.sommet = Cellule(ajout, self.sommet)
        self.taille += 1

    def depiler(self):
        y = self.sommet
        self.sommet = self.sommet.suivant
        self.taille -= 1
        return y

    def __len__(self):
        return self.taille

    """def __str__(self):
        aff = "Sommet: "+str(self.sommet)
        aff += "Taille: "+str(self.taille)
        return aff"""


pile_test = Pile()
print(len(pile_test))
print(pile_test.estVide())
pile_test.empiler('A')
pile_test.empiler('B')
pile_test.empiler('C')
pile_test.empiler('D')
print(len(pile_test))
print(pile_test.estVide())
print(pile_test.valeurSommet())
print(pile_test.depiler())
print(pile_test.valeurSommet())
print(len(pile_test))
