class Cellule:
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant
        
c3 = Cellule(5, None)
c2 = Cellule(7, c3)
c1 = Cellule(19, c2)
print(c1.valeur)
print(c1.suivant.valeur)
print(c1.suivant.suivant.valeur)
print(c1.suivant.suivant.suivant)
c1.suivant.valeur

class Pile:
    def __init__(self, sommet=None,taille=0):
        self.sommet = Cellule(sommet)
        self.taille = taille
        
    def estVide(self):
        if self.taille==0:return True
        else:return False
    def valeurSommet(self):
        return self.sommet
    
