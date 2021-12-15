from time import time_ns

def mesure(fonction,jeu):
    """ renvoie la durée du traitement"""
    debut = time_ns()
    fonction(jeu)
    fin = time_ns()
    return fin-debut