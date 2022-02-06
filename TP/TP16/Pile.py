def creer_pile():
    return []

def taille_pile(p):
    return len(p)

def pile_vide(p):
    return taille_pile(p) == 0

def empiler(p, x):
    p.append(x)
    
def depiler(p):
    if pile_vide(p):
        return None
    else:
        return p.pop()
    
def sommet_pile(p):
    if pile_vide(p):
        return None
    else:
        return p[-1]
		
def reinitialiser_pile(p):
	del p[:]
    