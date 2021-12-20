class Cellule:
    def __str__(self):
        return str(self.valeur)

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant
        
class File:
    def __init__(self, tete=0,queue=0,taille=0):
        self.tete = Cellule(tete,0)
        self.queue = Cellule(queue,0)
        self.taille = taille
        
    def estVide(self):
        if self.taille == 0:
            return True
        else:
            return False
        
    def valeurTete(self):
        val=self.tete.valeur
        return val
    
    def ajouterFile(self,element):
        self.taille+=1
        c=Cellule(element,None)
        if self.estVide():
            self.tete=c
        else:
            self.queue.suivant=c
        self.queue=c
        
    def retirerFile(self):
        self.taille-=1
        if not self.estVide():
            valeur=self.tete.valeur
            self.tete=self.tete.suivant
            return valeur
        else:
            return None
            
    def __len__(self):
        return self.taille
    
file_test = File()
print(len(file_test))
file_test.estVide()
file_test.ajouterFile('A')
file_test.ajouterFile('B')
file_test.ajouterFile('C')
file_test.ajouterFile('D')
print(len(file_test))
print(file_test.estVide())
print(file_test.valeurTete())
print(file_test.retirerFile())
print(file_test.valeurTete())
print(len(file_test))