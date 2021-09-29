def creer_pile():
    x = []
    return x


def taille_pile(p):
    return len(p)


def pile_vide(p):
    if len(p) == 0:
        return True
    else:
        return False


def empiler_pile(p, x):
    p.append(x)
    return p


def depiler(p):
    return p.pop()


def sommet_pile(p):
    return p[-1]

# Niels Carlon-Mismer