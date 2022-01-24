# Premier algorithme (ne marche pas mais celui que je pensais allait marcher sans aucune erreur)
def trouvercarres(x, y):
    xlist = list()
    ylist = list()
    grosse_liste = list()
    print(len(x), len(y))
    for i in range(len(x)):
        try:
            xlist.append(x[i + 1] - x[i])
        except IndexError: 
            xlist.append(x[i])
    for i in range(len(y)):
        try:
            ylist.append(y[i + 1] - y[i])
        except IndexError:
            ylist.append(y[i])
    print(xlist, ylist)
    grosse_liste += xlist + ylist
    grosse_liste = xlist + list(set(ylist) - set(xlist))
    print(grosse_liste)
    sol =0
    for xgrosse in grosse_liste:
        for ygrosse in grosse_liste:
            if xgrosse == ygrosse: 
                sol +=1 
    return sol

# Deuxième algorithme (j'ai demandé de l'aide a Aaliyah parce que je n'arrivais rien a faire après pas mal de codes différents)
def algo2(x,y):
    """
    Trouve le nombre de carres dans deux listes pour chaque absisse

    Args:
        x (list): liste des cordonnees en x
        y (lsit): liste des coordonnees en y

    Returns:
        int: Nombre de carres
    """
    liste_x = []
    liste_y = []
    resul = 0
    # Crée une liste qui contient toutes les valeurs possibles pour des longueurs.
    for i in range(len(x)):
        for j in range(len(x)):
            if x[j] - x[i] > 0:
                liste_x.append(x[j] - x[i])
                print("liste_x:",liste_x)

    # Crée une liste qui contient toutes les valeurs possibles pour des largeurs.
    for i in range(len(y)):
        for j in range(len(y)):
            if y[j] - y[i] > 0:
                liste_y.append(y[j] - y[i])
                print("liste_y:", liste_y)

    # Ici on compare les 2 listes et si les valeurs sont identiques on ajoute 1 au compteur résul
    for i in range(len(liste_x)):
        for j in range(len(liste_y)):
            if liste_x[i] == liste_y[j]:
                resul += 1
                
    return resul

# Niels - Romain