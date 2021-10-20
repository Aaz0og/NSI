from random import *
from typing import Dict

class Personnage:
    def __init__(self):
        self.pv=randint(20,30)
        self.cons=randint(1,5)
        self.déf=randint(1,3)
        self.atk=randint(3,6)
        self.vatk=randint(1,10000)
        self.arme=None
        self.armure=None
        self.zone=randint(1,9)

    def showpv(self):
        return(self.pv)

    def showstats(self):
        return(self.pv,self.atk,self.déf,self.vatk,self.cons)

    def showpos(self):
        return(self.zone)

    def showstuff(self):
        return(self.arme,self.armure)

    def takedamage(self,dégats):
        self.pv=self.pv-dégats

    def fight(self,other):
        if other.vatk>self.vatk:
            self.takedamage(2+other.atk-self.déf)
            other.takedamage(2+self.atk-other.déf)
        else:
            other.takedamage(2+self.atk-other.déf)
            self.takedamage(2+other.atk-self.déf)

    def app(self,list):
        list.append(self)




class GameEvents:
    def __init__(self):
        self.foundweapons=0
        self.foundarmors=0
        self.tours=0

    def tourcombat():
        pass


MrEven=Personnage()
Romain=Personnage()
Angel=Personnage()

liste=[MrEven,Romain,Angel]

def test(sah,prec=liste[1]):
    
    for pers in liste:
        if pers.zone == prec.zone:
            print("Même")
        prec=pers
        
test(2)