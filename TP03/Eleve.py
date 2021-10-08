class Eleve:
    def __init__(self, nom, prenom, notes=list()):
        self.nom = str(nom)
        self.prenom = str(prenom)
        self.notes = notes

    def ajouterNote(self, x):
        self.notes.append(x)

    def moyenne(self):
        tot = sum(self.notes)
        if tot == 0:
            return 0
        return tot/len(self.notes)

    def noteLaPlusBasse(self):
        return min(self.notes)

    def noteLaPlusHaute(self):
        return max(self.notes)

    def __str__(self):
        aff = str(self.nom)+" "+str(self.prenom) + \
            " - Moyenne : "+str(self.moyenne())
        return aff


class Note:
    def __init__(self, valeur, coefficient, matiere):
        self.valeur = valeur
        self.coefficient = coefficient
        self.matiere = matiere


eleve1 = Eleve("John", "Smith")
print(eleve1.moyenne())
eleve1.ajouterNote(11)
eleve1.ajouterNote(13)
eleve1.ajouterNote(8)
eleve1.ajouterNote(15)
print(eleve1.moyenne())
print(eleve1.noteLaPlusHaute())
print(eleve1.noteLaPlusBasse())
print(eleve1)
