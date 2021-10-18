from afficheur_arbre import afficher_arbre


class NoeudBinaire:
    def __init__(self, valeur, fils_gauche, fils_droite):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droite = fils_droite
    
D = NoeudBinaire("D", None, None)
C = NoeudBinaire("C", D, None)
B = NoeudBinaire("B", None, None)
A = NoeudBinaire("A", B, C)
mon_arbre = A
afficher_arbre(mon_arbre)
