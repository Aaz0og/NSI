class Cellule:
    def __str__(self):
        return str(self.valeur)

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

class Pile:
    def __init__(self, sommet=0, taille=0):
        self.sommet = Cellule(sommet, None)
        self.taille = taille

    def estVide(self):
        """
        Regarde la taille de la file pour voir si elle est vide

        Returns:
            bool: True si vide False si non vide
        """
        if self.taille == 0:
            return True
        else:
            return False

    def valeurSommet(self):
        """
        Regarde la valeur du sommet

        Returns:
            int: Valeur du sommet
        """
        return self.sommet.valeur

    def empiler(self, ajout):
        """
        Ajoute le numéro voulu au dessus du numéro actuel

        Args:
            ajout (int): nombre que l'on souhaite ajouter a la pile
        """
        self.sommet = Cellule(ajout, self.sommet)
        self.taille += 1

    def depiler(self):
        """
        Retire le sommet de la pile

        Returns:
            int: Sommet de la pile qui a été retiré
        """
        y = self.sommet
        self.sommet = self.sommet.suivant
        self.taille -= 1
        return y

    def __len__(self):
        """
        Sers a configurer la commande len

        Returns:
            int: Taille de la file
        """
        return self.taille

#! Tests

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

# Niels Carlon-Mismer