from afficheur_arbre import afficher_arbre


class NoeudBinaire:
    def __init__(self, valeur, fils_gauche, fils_droite):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droite = fils_droite

    def taille(self):
        taille = 1
        if self.fils_gauche != None:
            taille += self.fils_gauche.taille()
        if self.fils_droite != None:
            taille += self.fils_droite.taille()
        return taille

    def hauteur(self, hauteurG=0, hauteurD=0):
        if self.fils_droite != None:
            hauteurD += self.fils_droite.hauteur()
        if self.fils_gauche != None:
            hauteurG += self.fils_gauche.hauteur()
        return max(hauteurD, hauteurG)+1


"""
D = NoeudBinaire("D", None, None)
C = NoeudBinaire("C", D, None)
B = NoeudBinaire("B", None, None)
A = NoeudBinaire("A", B, C)
mon_arbre = A
"""

J = NoeudBinaire("J", None, None)
H = NoeudBinaire("H", None, J)
I = NoeudBinaire("I", None, None)
G = NoeudBinaire("G", I, None)
F = NoeudBinaire("F", G, H)
E = NoeudBinaire("E", None, None)
C = NoeudBinaire("C", E, None)
D = NoeudBinaire("D", None, None)
B = NoeudBinaire("B", C, D)
A = NoeudBinaire("A", B, F)
mon_arbre = A

#afficher_arbre(mon_arbre)
#print(mon_arbre.taille())
#print(mon_arbre.hauteur())


class NBR(NoeudBinaire):
    def __init__(self, valeur):
        self.valeur = valeur
        self.fils_gauche = fils_gauche = None
        self.fils_droite = fils_droite = None


abr = NBR(5)
print(abr.hauteur())
print(abr.taille())
abr = NBR(10)
# afficher_arbre(abr)

arbre_binaire_recherche = None
