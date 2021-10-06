class Cellule:
    def __str__(self):
        aff = str(self.valeur)
        return aff

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant
        
class File:
    def __init__(self, tete=None,queue=None,taille=0):
        self.tete = Cellule(tete,None)
        self.queue = Cellule(queue,None)
        self.taille = taille
        
    def estVide(self):
        if self.taille == 0:
            return True
        else:
            return False
        
    def valeurTete(self):
        return self.tete.valeur
    
    def __len__(self):
        return self.taille