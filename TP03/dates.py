class Dates:
    def __str__(self):
        afficher = str(self.jour)+"/"+str(self.mois)+"/"+str(self.année)+" : "+ 
    def __init__(self,jour,mois,année,nombre):
        self.jour  = jour
        self.mois = mois 
        self.année = année 
        self.nombre = int(nombre)
    
    def nomMois(self):
        return mois.values(str(self.mois))
    
mois = {"1": "Janvier","2":"Février","3":"Mars","4":"Avril",
        "5":"Mai","6":"Juin","7":"Juillet","8":"Août","9":"Septembre",
        "10":"Octobre","11":"Novembre","12":"Décembre"}
