class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivant = s


longueurdelaliste = 1

def nieme(lst):
    pass
def longueur(lst):
    global longueurdelaliste
    if lst.valeur == None:
        return str("La liste est vide")
    elif lst.suivant != None:
        longueurdelaliste += 1
        longueur(lst.suivant)
    else:
        print(longueurdelaliste)
        pass


MaListe = Cellule(1, Cellule(2, Cellule(3, None)))
ListeTest = Cellule(None, None)
print(MaListe.valeur)
print(longueur(ListeTest))
longueur(MaListe)
