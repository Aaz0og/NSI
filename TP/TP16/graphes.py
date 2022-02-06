from afficheur_graphe import afficher_graphe, afficher_graphe_non_oriente
from FileProf import FileProf
from Pile import *


class GrapheOriente:
    def __init__(self):
        self.dico_adjacence = dict()

    def ajouter_sommet(self, sommet):
        """
        Ajouter un sommet a un graphe

        Args:
            sommet (int,str): Nom du sommet a ajouter

        Returns:
            dict: Dictionnaire rentré avec nouveau sommmet
        """
        
        if sommet not in self.dico_adjacence:
            self.dico_adjacence[sommet] = []
        return self.dico_adjacence

    def sommets(self):
        """
        Renvoi tout les sommets du dict rentré

        Returns:
            dict: Dictionnaire d'un graphe
        """
        return sorted(self.dico_adjacence.keys())

    def contient_sommet(self, sommet):
        """
        Regarde si un dictionnaire de sommets contient un certain sommet

        Args:
            sommet (int,str): Sommet que l'ont veut trouver dans le dict

        Returns:
            dict: Renvoie la liste des sommets d'un dictionnaire
        """
        return sommet in self.dico_adjacence

    def ajouter_arc(self, sommet_1, sommet_2):
        """
        Ajoute un arc entre deux sommets

        Args:
            sommet_1 (int,str): Sommet 1
            sommet_2 (int,str): Sommet 2

        Returns:
            dict: Nouvel arc créé
        """
        if GrapheOriente.contient_sommet(self, sommet_1) is False:
            GrapheOriente.ajouter_sommet(self, sommet_1)
        if GrapheOriente.contient_sommet(self, sommet_2) is False:
            GrapheOriente.ajouter_sommet(self, sommet_2)
        return self.dico_adjacence[sommet_1].append(sommet_2)

    def arc_existe(self, sommet_1, sommet_2):
        """
        Regarde si un arc existe entre deux sommets

        Args:
            sommet_1 (int,str): Sommet 1
            sommet_2 (int,str): Sommet 2

        Returns:
            bool: Vrai si un arc existe Faux dans le cas contraire
        """
        return sommet_2 in self.dico_adjacence[sommet_1]

    def voisins(self, sommet):
        """
        Renvoi la liste des voisins d'un sommet

        Args:
            sommet (int,str): Sommet

        Returns:
            lst: Liste des sommets voisins du sommet
        """
        return sorted(self.dico_adjacence[sommet])

    def degre(self, sommet):
        """
        Renvoi le degré d'un sommet

        Args:
            sommet (int,str): Sommet

        Returns:
            int: Degré du sommet rentré
        """
        res = 0
        for cles in self.dico_adjacence.keys():
            if sommet in self.dico_adjacence[cles]:
                res += 1
        return res + len(self.dico_adjacence[sommet])
    
    def parcours_largeur(self,sommet):   
        file = FileProf()
        file.ajouterFile(sommet)
        sommets_rencontres = {}
        sommets_rencontres[sommet] = True
        while not file.estVide():
            courant = file.retirerFile()
            print(courant)
            for voisin in self.voisins(courant):
                if voisin not in sommets_rencontres:
                    file.ajouterFile(voisin)
                    sommets_rencontres[voisin] = True

# Graphe Orienté sur PDF
graphe_oriente_tp = GrapheOriente()
graphe_oriente_tp.ajouter_arc("A", "B")
graphe_oriente_tp.ajouter_arc("B", "A")
graphe_oriente_tp.ajouter_arc("B", "F")
graphe_oriente_tp.ajouter_arc("B", "G")
graphe_oriente_tp.ajouter_arc("F", "C")
graphe_oriente_tp.ajouter_arc("C", "D")
graphe_oriente_tp.ajouter_arc("D", "E")
graphe_oriente_tp.ajouter_arc("G", "C")
graphe_oriente_tp.ajouter_arc("G", "H")
graphe_oriente_tp.ajouter_arc("G", "D")
graphe_oriente_tp.ajouter_arc("H", "G")
# ---

# afficher_graphe(graphe_oriente_tp)
"""
print(graphe_oriente_tp.voisins("A"))
print(graphe_oriente_tp.degre("G"), graphe_oriente_tp.degre("A"),
      graphe_oriente_tp.degre("B"), graphe_oriente_tp.degre("E"))
"""


class GrapheNonOriente(GrapheOriente):
    def ajouter_arc(self, sommet_1, sommet_2):
        if GrapheOriente.contient_sommet(self, sommet_1) is False:
            GrapheOriente.ajouter_sommet(self, sommet_1)
        if GrapheOriente.contient_sommet(self, sommet_2) is False:
            GrapheOriente.ajouter_sommet(self, sommet_2)
        self.dico_adjacence[sommet_1].append(sommet_2)
        self.dico_adjacence[sommet_2].append(sommet_1)
        return self.dico_adjacence

    def degre(self, sommet):
        return len(self.dico_adjacence[sommet])


# Graphe non orienté du PDF
graphe_non_oriente_tp = GrapheNonOriente()
graphe_non_oriente_tp.ajouter_arc("A", "B")
graphe_non_oriente_tp.ajouter_arc("A", "F")
graphe_non_oriente_tp.ajouter_arc("B", "C")
graphe_non_oriente_tp.ajouter_arc("B", "G")
graphe_non_oriente_tp.ajouter_arc("B", "D")
graphe_non_oriente_tp.ajouter_arc("F", "G")
graphe_non_oriente_tp.ajouter_arc("F", "H")
graphe_non_oriente_tp.ajouter_arc("I", "H")
graphe_non_oriente_tp.ajouter_arc("C", "E")
graphe_non_oriente_tp.ajouter_arc("D", "I")
graphe_non_oriente_tp.ajouter_arc("I", "E")
graphe_non_oriente_tp.ajouter_arc("G", "I")
# ---
"""
print(graphe_non_oriente_tp.degre("A"), graphe_non_oriente_tp.degre("B"),
      graphe_non_oriente_tp.degre("G"), graphe_non_oriente_tp.degre("H"))
print(graphe_non_oriente_tp.voisins("B"))
"""

print(graphe_oriente_tp.sommets())