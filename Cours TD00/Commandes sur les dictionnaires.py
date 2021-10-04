""" Créations d'un dictionnaire vide"""
d = dict()
d = {}

""" Création d'un dictionnaire avec des clés et valeurs"""
d1 = {"P1" : ["Marie", "Smith"], "P2": ["John", "Smith"]}

""" ajout d'un couple clé/valeur"""
d1["P3"]= ["John", "Doe"]
d1[-13]= "Hello world"  # les clés et valeur peuvent être de n'importe quel type

""" accès à l'ensembe des clés/ valeurs"""
d1.keys()
d1.values()

""" affichage """
print(d1)