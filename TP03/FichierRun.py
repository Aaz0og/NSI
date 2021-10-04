mois = {1: "Janvier",2:"Février",3:"Mars",4:"Avril",
        5:"Mai",6:"Juin",7:"Juillet",8:"Août",9:"Septembre",
        10:"Octobre",11:"Novembre",12:"Décembre"}

class Date:
    def __str__(self):
        afficher = str(self.jour)+"/"+str(self.mois)+"/"+str(self.année)+" : "+str(self.jour)+" "+str(mois[self.mois])+" "+str(self.année)
        return afficher
    def __init__(self,jour,mois,année):
        self.jour  = jour
        self.mois = mois 
        self.année = année 
        #self.nombre = int(nombre)

    def nomMois(self):
        return mois.values(str(self.mois))
    
    def __lt__(self, datecomparee):
        if self < datecomparee:
            return True
        else: 
            return False


d1 = Date(3,2,2024)
print(d1)
d2 = Date(8,9,2024)
print(d1<d2)