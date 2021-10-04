"""
class Fraction:
    def __str__(self):
        affichage = "Fraction"+"\n"
        affichage+= "Valeur"+ str(self.valeur())+"\n"
        affichage+= "Multiplier"+str(self.multiplier())+"\n"
    def __init__(self,numerateur,denominateur):
        self.denominateur = denominateur
        self.numerateur = numerateur
        
    def valeur(self):
        return self.numerateur%self.denominateur

    def multiplier(self, fraction_bis):
        return Fraction(self.denominateur*fraction_bis.denominateur, self.numerateur*fraction_bis.numerateur)
    
f1 = Fraction(1,3)
print(f1)
"""