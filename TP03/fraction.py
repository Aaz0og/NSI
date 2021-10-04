class Fraction:
    def __init__(self, nume, deno):
        self.numerateur = nume
        self.denominateur = deno

    def valeur(self):
        return self.numerateur/self.denominateur

    def multiplier(self, fraction_bis):
        numerateur = self.numerateur*fraction_bis.numerateur
        denominateur = self.denominateur*fraction_bis.denominateur
        resultat = Fraction(numerateur, denominateur)
        return resultat

    def __str__(self):
        afficher = "Fraction: " + str(self.numerateur)+ "/" +str(self.denominateur) + "\n"
        afficher +="Valeur: " + str(self.valeur())
        #afficher +="Multiplier : "+str(self.multiplier())+"\n"
        return afficher

f1 = Fraction(1, 3)
print(f1)
print(f1.valeur())
f2 = Fraction(3,2)
print(f2.valeur())
f3 = f1.multiplier(f2)
print(f3)
print(f3.valeur())