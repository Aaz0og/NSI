import urllib.parse
import webbrowser

def traverser_graphe(graphe, oriente):
    if oriente:
        type_graphe = "digraph"
        lien = "->"
    else:
        type_graphe = "strict graph"
        lien = "--"
    donnees_graphe = type_graphe + " G { \n"
    if len(graphe.sommets()) != 0:
        num_sommets = dict()
        l_adja = list(graphe.dico_adjacence)
        for i in range(len(l_adja)):
            sommet_courant = l_adja[i]
            num_sommets[sommet_courant] = i
            donnees_graphe += "N%d [label=\"%s\"]\n" % (i , str(sommet_courant))
        for i in range(len(l_adja)):
            sommet_courant = l_adja[i]
            for voisin in graphe.dico_adjacence[sommet_courant]:
                if voisin in num_sommets:
                    numero = num_sommets[voisin]                              
                    donnees_graphe += "N%d %s N%d\n" % (i, lien, numero)


    donnees_graphe += "}\n"
    return donnees_graphe
        
def generer_lien(graphe, oriente):
    donnees_formatees = urllib.parse.quote(traverser_graphe(graphe, oriente))
    lien_graphiz = "https://dreampuf.github.io/GraphvizOnline/#"+ donnees_formatees
    return lien_graphiz
  

def afficher_graphe_oriente(graphe):
    lien_graphe = generer_lien(graphe, True)
    webbrowser.open(lien_graphe)

def afficher_graphe_non_oriente(graphe):
    lien_graphe = generer_lien(graphe, False)
    webbrowser.open(lien_graphe)
    
def afficher_graphe(graphe):
    if type(graphe).__name__ == 'GrapheNonOriente':
        afficher_graphe_non_oriente(graphe)
    elif type(graphe).__name__ == 'GrapheOriente':
        afficher_graphe_oriente(graphe)